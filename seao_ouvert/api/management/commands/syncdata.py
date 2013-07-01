# TODO: clean up the import section.
from django.core.management.base import BaseCommand
from zipfile import ZipFile
from seao_ouvert.api.models import *
from optparse import make_option
import datetime, urllib2
from xml.etree import ElementTree
from bs4 import BeautifulSoup
import pdb
from django.utils import timezone
from urlparse import urlparse, parse_qs
from os import listdir


class Command(BaseCommand):

    URL_SEAO = 'http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995'
    LOCAL_PATH = "data/"

    option_list = BaseCommand.option_list +  (

        )

    help = BaseCommand.help + "Effectue la synchronisation entre la bd locale et les donnees de seao"

    def handle(self, *args, **options):
        print "SEAO Ouvert"
        print "START import of data from source to local"
        print "================================"
        urls = self.get_urls()
        print "--------------------------------"
        urls = self.get_urls_to_download(urls)
        print "--------------------------------"
        if urls:
            self.download_files(urls)
            print "--------------------------------"
        files_extracted = self.extract_files(urls)
        print "--------------------------------"
        self.load_files(files_extracted)


        print "================================"
        print "END of local import from data source"

    def load_files(self, files):
        
        print "Loading downloaded files into database"

        if not files:
            print "** No files to load into database"
            return
            
        for file in files:
            self.load_file(file)
        
        print "{0} files loaded into database".format(len(files))

    def load_file(self, file):
        
        print "Loading \"{0}\" into database".format(file)
    
        fichier = ElementTree.parse(self.LOCAL_PATH + file)

        data = fichier.getroot()
        data_len = len(data)

        print('0%'),

        for line_number, avis in enumerate(data):
            
            print ("\r{0}%".format(int(line_number/float(data_len)*100))),

            self.loader_avis(avis, line_number)
        

        print('\r100%')
        print "\"{0}\" loaded successfully".format(file)

    def loader_avis(self, avis, line_number):

        nouveau = Avis()
        nouveau.numero_seao = avis.find( 'numeroseao' ).text
        nouveau.numero = avis.find( 'numero' ).text
    
        nouveau.organisme = avis.find( 'organisme' ).text
        nouveau.municipal = int(avis.find( 'municipal' ).text)
        nouveau.ville = avis.find( 'ville' ).text
        nouveau.adresse1 = avis.find( 'adresse1' ).text
        if nouveau.adresse1:
            nouveau.adresse1.encode("ascii","ignore")
        nouveau.adresse2 = avis.find( 'adresse2' ).text
        if nouveau.adresse2:
            nouveau.adresse2.encode("ascii","ignore")
        nouveau.code_postal = avis.find( 'codepostal' ).text
        
        code_p = avis.find( 'province' ).text
        if code_p:
            nouveau.province, created = Province.objects.get_or_create\
                                   (code=code_p ,defaults={'name': 'default'})

        code_p = avis.find( 'pays' ).text
        if code_p:
            nouveau.pays, created = Pays.objects.get_or_create\
                                   (code=code_p ,defaults={'name': 'default'})
        
        code_t = avis.find( 'type' ).text
        if code_t:
            nouveau.type, created = Type.objects.get_or_create\
                                   (code=code_t ,defaults={'name': 'default'})

        code_n = avis.find( 'nature' ).text
        if code_n:
            nouveau.nature, created = Nature.objects.get_or_create\
                                   (code=code_n ,defaults={'name': 'default'})

        date_publication = datetime.datetime.strptime(avis.find( 'datepublication' ).text, "%Y-%m-%d %H:%M")
        date_publication = date_publication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_publication = date_publication

        date_fermeture = datetime.datetime.strptime(avis.find( 'datefermeture' ).text, "%Y-%m-%d %H:%M")
        date_fermeture = date_fermeture.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_fermeture = date_fermeture

        date_saisie_adjudication = datetime.datetime.strptime(avis.find( 'datesaisieadjudication' ).text, "%Y-%m-%d %H:%M")
        date_saisie_adjudication = date_saisie_adjudication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_saisie_adjudication = date_saisie_adjudication

        date_adjudication = datetime.datetime.strptime(avis.find( 'dateadjudication' ).text, "%Y-%m-%d")
        date_adjudication = date_adjudication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_adjudication = date_adjudication 

        #What's up avec le m2m et regions??
        
        code_d = avis.find( 'disposition' ).text
        if nouveau.municipal and code_d:

            nouveau.disposition_municipale, created = DispositionMunicipale.objects.get_or_create\
                                                (code=code_d ,defaults={'name': 'default'})
        elif code_d:

            nouveau.disposition_non_municipale, created = DispositionNonMunicipale.objects.get_or_create\
                                                (code=code_d ,defaults={'name': 'default'})

        #Sauvegarder l'avis avait de lui attribuer des fournisseurs
        nouveau.save()

        for fournisseur in avis.find( 'fournisseurs' ):
            self.loader_fournisseur(nouveau, fournisseur)
           
    def loader_fournisseur(self, avis, fournisseur):

        nouvelle = Soumission()

        nomorganisation = fournisseur.find( 'nomorganisation' ).text

        if not nomorganisation:
            nouvelle.nom_organisation = "default"
        else:
            nouvelle.nom_organisation = nomorganisation
        
        nouvelle.adresse1 = fournisseur.find( 'adresse1' ).text
        nouvelle.adresse2 = fournisseur.find( 'adresse2' ).text
        nouvelle.ville = fournisseur.find( 'ville' ).text
        nouvelle.code_postal = fournisseur.find( 'codepostal' ).text
        nouvelle.admissible = fournisseur.find( 'admissible' ).text
        nouvelle.conforme = fournisseur.find( 'conforme' ).text
        nouvelle.adjudicataire = fournisseur.find( 'adjudicataire' ).text
        nouvelle.montant_soumis = fournisseur.find( 'montantsoumis' ).text
        nouvelle.montant_contrat = fournisseur.find( 'montantcontrat' ).text
        
        code_p = fournisseur.find( 'province' ).text
        if code_p:
            nouvelle.province, created = Province.objects.get_or_create\
                                (code=code_p ,defaults={'name': 'default'})

        code_p = fournisseur.find( 'pays' ).text
        if code_p:
            nouvelle.pays, created = Pays.objects.get_or_create\
                                (code=code_p ,defaults={'name': 'default'})

        unite = fournisseur.find( 'montantssoumisunite' ).text
        if not unite:
            nouvelle.montant_soumis_unite, created = UniteMontant.objects.get_or_create\
                                (code=unite ,defaults={'name': 'default'})

        nouvelle.appel = avis
        nouvelle.save()

    def get_urls(self):
        '''
        Return urls for files to download from seao.
        '''
        
        print "Finding urls of files to download from seao"

        page = urllib2.urlopen(self.URL_SEAO).read()
        soup = BeautifulSoup(page)

        urls = []

        for a in soup.find_all("img", src="images/download.png"):
            urls.append(a.find_parent("a")['href'])

        print "From :"
        print self.URL_SEAO
        print "Found :"
        for url in urls:
            print "* %s" % (url,)

        return urls
    
    def get_urls_to_download(self, urls):
        '''
        Checks which files have to be downloaded
        '''

        urls_to_download = []
        
        local_files = listdir(self.LOCAL_PATH)

        for url in urls:
            parsed_url = urlparse(url)
            filename = parse_qs(parsed_url.query)['fname'][0]
            if filename not in local_files:
                urls_to_download.append(url)

        print "Files to download :"
        for url in urls_to_download:
            print "* %s" % (url,)

        if not urls_to_download:
            print "** No files to download from source"

        return urls_to_download
    
    def download_files(self, urls):
        print "Downloading data files from source :"
    
        for url in urls:
            
            parsed_url = urlparse(url)
            filename = parse_qs(parsed_url.query)['fname'][0]
            
            # Convert to non-unicode
            filename = str(filename)

            local_path = "%s%s" % (self.LOCAL_PATH, filename,)
    
            zip_file = urllib2.urlopen(url)
            
            with open(local_path,'wb') as f: f.write(zip_file.read())
    
            print "From :"
            print url
            print "Download to :"
            print local_path
        
    def extract_files(self, urls):
        print "Extracting data from local files :"
        
        if not urls:
            print "** No files to extract."
            return

        files_extracted = []
    
        for url in urls:

            parsed_url = urlparse(url)
            filename = parse_qs(parsed_url.query)['fname'][0]
            
            zip_file_path = "%s%s" % (self.LOCAL_PATH, filename)
    
            with ZipFile(zip_file_path, 'r') as zip_file:
                
                zip_file.extractall(self.LOCAL_PATH)

                for file in zip_file.namelist():
                    files_extracted.append(file)
                
            print "From :"
            print zip_file_path
            print "Extracting all files to :"
            print "%s" % (self.LOCAL_PATH,)
        
        return files_extracted

        
