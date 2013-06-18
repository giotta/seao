from django.core.management.base import BaseCommand
from seao_ouvert.api.models import *
from optparse import make_option
import urllib2, json, datetime
import pdb
from django.utils import timezone

class Command(BaseCommand):

    URL_AVIS = "http://seao.pourvotre.info/avis.json"

    option_list = BaseCommand.option_list +  (

        make_option('-f', '--fichier',
        action='store',
        dest='fichier',
        default=None,
        help='Load les avis depuis un fichier source .json'),

        make_option('-x', '--xml',
        action='store_true',
        dest='xml',
        default=True,
        help='Load les avis depuis un fichier xml dorigine'),

        )

    help = BaseCommand.help + "Load les donnees des avis a partir dun fichier json"

    def handle(self, *args, **options):
        
        if options['fichier']:
            stream = open(options['fichier'])
        else:
            stream = urllib2.urlopen(self.URL_AVIS)
        
        for avis in stream.readlines():
            avis = json.loads(avis)
            self.loader_avis(avis)

    def loader_avis(self, avis):

        nouveau = Avis()
        nouveau.numero_seao = avis['numeroseao']

        if not avis['numero']:
            #Il devrait toujours y avoir un numero pour un avis.
            return

        nouveau.numero = avis['numero']
        nouveau.organisme = avis['organisme']
        nouveau.municipal = avis['municipal']
        nouveau.adresse1 = avis['adresse1']
        nouveau.adresse2 = avis['adresse2']
        nouveau.code_postal = avis['codepostal']
        
        code_p = avis['province']
        if code_p:
            nouveau.province, created = Province.objects.get_or_create\
                                   (code=code_p ,defaults={'name': 'default'})

        code_p = avis['pays']
        if code_p:
            nouveau.pays, created = Pays.objects.get_or_create\
                                   (code=code_p ,defaults={'name': 'default'})
        
        code_t = avis['type']
        if code_t:
            nouveau.type, created = Type.objects.get_or_create\
                                   (code=code_t ,defaults={'name': 'default'})

        code_n = avis['nature']
        if code_n:
            nouveau.nature, created = Nature.objects.get_or_create\
                                   (code=code_n ,defaults={'name': 'default'})

        date_publication = datetime.datetime.strptime(avis['datepublication'], "%Y-%m-%d %H:%M")
        date_publication = date_publication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_publication = date_publication

        date_fermeture = datetime.datetime.strptime(avis['datefermeture'], "%Y-%m-%d %H:%M")
        date_fermeture = date_fermeture.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_fermeture = date_fermeture

        date_saisie_adjudication = datetime.datetime.strptime(avis['datesaisieadjudication'], "%Y-%m-%d %H:%M")
        date_saisie_adjudication = date_saisie_adjudication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_saisie_adjudication = date_saisie_adjudication

        date_adjudication = datetime.datetime.strptime(avis['dateadjudication'], "%Y-%m-%d")
        date_adjudication = date_adjudication.replace(tzinfo=timezone.get_current_timezone())
        nouveau.date_adjudication = avis['dateadjudication']

        #What's up avec le m2m et regions??
        
        code_d = avis['disposition']
        if nouveau.municipal and code_d:

            nouveau.disposition_municipale, created = DispositionMunicipale.objects.get_or_create\
                                                (code=code_d ,defaults={'name': 'default'})
        elif code_d:

            nouveau.disposition_non_municipale, created = DispositionNonMunicipale.objects.get_or_create\
                                                (code=code_d ,defaults={'name': 'default'})

        #Saving new avis before associating fournisseur to it.
        nouveau.save()

        for nom, fournisseur in avis['fournisseurs'].items():
            self.loader_fournisseur(nouveau, fournisseur)
           
    def loader_fournisseur(self, avis, fournisseur):

        # Pour Gerer l'inconsistence dans les datas
        if isinstance(fournisseur, list):
            fournisseur = fournisseur[0]

        nouvelle = Soumission()
        if not fournisseur['nomorganisation']:
            #Il devrait toujours y avoir un nom pour les fournisseur
            return
        
        nouvelle.nom_organisation = fournisseur['nomorganisation']
        nouvelle.adresse1 = fournisseur['adresse1']
        nouvelle.adresse2 = fournisseur['adresse2']
        nouvelle.ville = fournisseur['ville']
        nouvelle.code_postal = fournisseur['codepostal']
        nouvelle.admissible = fournisseur['admissible']
        nouvelle.conforme = fournisseur['conforme']
        nouvelle.adjudicataire = fournisseur['adjudicataire']
        nouvelle.montant_soumis = fournisseur['montantsoumis']
        nouvelle.montant_contrat = fournisseur['montantcontrat']
        
        code_p = fournisseur['province']
        if code_p:
            nouvelle.province, created = Province.objects.get_or_create\
                                (code=code_p ,defaults={'name': 'default'})

        code_p = fournisseur['pays']
        if code_p:
            nouvelle.pays, created = Pays.objects.get_or_create\
                                (code=code_p ,defaults={'name': 'default'})

        unite = fournisseur['montantssoumisunite']
        if not unite:
            nouvelle.montant_soumis_unite, created = UniteMontant.objects.get_or_create\
                                (code=unite ,defaults={'name': 'default'})

        nouvelle.appel = avis
        nouvelle.save()
