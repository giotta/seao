from django.core.management.base import BaseCommand
from seao_ouvert.api.models import *
from optparse import make_option
import datetime
import pdb
from xml.etree import ElementTree
from django.utils import timezone

class Command(BaseCommand):

    option_list = BaseCommand.option_list +  (

        make_option('-f', '--fichier',
        action='store',
        dest='fichier',
        default=False,
        help='Fichier xml qui contient les avis'),

        )

    help = BaseCommand.help + "Load les donnees des avis a partir dun fichier xml"

    def handle(self, *args, **options):
        
        if not options['fichier']:
            self.stdout.write("Veuillez specifier un fichier avec loption -f")
            return
        else:
            fichier = ElementTree.parse(options['fichier'])
        
        for line_number, avis in enumerate(fichier.getroot()):
            self.loader_avis(avis, line_number)

    def loader_avis(self, avis, line_number):

        nouveau = Avis()
        nouveau.numero_seao = avis.find( 'numeroseao' ).text
        nouveau.numero = avis.find( 'numero' ).text

        if not nouveau.numero:
            self.stderr.write("Aucun numero d'avis : ligne {0}".append(line_number))
            return
    
        nouveau.orgamisme = avis.find( 'organisme' ).text
        nouveau.municipal = avis.find( 'municipal' ).text
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
            self.stderr.write("aucun nom pour un fournisseur:")
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
