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
            return
        nouveau.numero = avis['numero']
        nouveau.organisme = avis['organisme']
        nouveau.municipal = avis['municipal']
        nouveau.adresse1 = avis['adresse1']
        nouveau.adresse2 = avis['adresse2']
        
        code_p = avis['province']
        if code_p and not Province.objects.filter(code=code_p):
            nouvelle_province = Province()
            nouvelle_province.code = code_p
            nouvelle_province.name = "province{0}".format(code_p)
            nouvelle_province.save()
        if code_p:
            nouveau.province = Province.objects.get(code=code_p)

        code_p = avis['pays']
        if not Pays.objects.filter(code=code_p):
            nouveau_pays= Pays()
            nouveau_pays.code = code_p
            nouveau_pays.name = "pays{0}".format(code_p)
            nouveau_pays.save()
        if code_p:
            nouveau.pays = Pays.objects.get(code=code_p)

        nouveau.code_postal = avis['codepostal']
        
        if not Type.objects.filter(code=avis['type']):
            nouveau_type= Type()
            nouveau_type.code = avis['type']
            nouveau_type.name = "type{0}".format(avis['type'])
            nouveau_type.save()
        nouveau.type = Type.objects.get(code=avis['type'])

        if not Nature.objects.filter(code=avis['nature']):
            nouvelle_nature= Nature()
            nouvelle_nature.code = avis['nature']
            nouvelle_nature.name = "nature{0}".format(avis['nature'])
            nouvelle_nature.save()
        nouveau.nature = Nature.objects.get(code=avis['nature'])

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
        
        if nouveau.municipal and avis['disposition']:

            if not DispositionMunicipale.objects.filter(code=avis['disposition']):
                nouvelle_dispo= DispositionMunicipale()
                nouvelle_dispo.code = avis['disposition']
                nouvelle_dispo.name = "disposition{0}".format(avis['disposition'])
                nouvelle_dispo.save()
            nouveau.disposition_municipale = DispositionMunicipale.objects.\
                                             get(code=avis['disposition'])
        elif avis['disposition']:

            if not DispositionNonMunicipale.objects.filter(code=avis['disposition']):
                nouvelle_dispo= DispositionNonMunicipale()
                nouvelle_dispo.code = avis['disposition']
                nouvelle_dispo.name = "disposition{0}".format(avis['disposition'])
                nouvelle_dispo.save()
            nouveau.disposition_non_municipale = DispositionNonMunicipale.objects.\
                                                   get(code=avis['disposition'])

        #Saving new avis before associating fournisseur to it.
        nouveau.save()

        for nom, fournisseur in avis['fournisseurs'].items():
            self.loader_fournisseur(nouveau.numero_seao, fournisseur)
           
    def loader_fournisseur(self, seao, fournisseur):

        # Pour Gerer l'inconsistence dans les datas
        if isinstance(fournisseur, list):
            fournisseur = fournisseur[0]

        nouvelle = Soumission()
        if not fournisseur['nomorganisation']:
            return
        nouvelle.nom_organisation = fournisseur['nomorganisation']
        nouvelle.adresse1 = fournisseur['adresse1']
        nouvelle.adresse2 = fournisseur['adresse2']
        nouvelle.ville = fournisseur['ville']
        
        code_p = fournisseur['province']
        if code_p and not Province.objects.filter(code=code_p).exists():
            nouvelle_province= Province()
            nouvelle_province.code = code_p
            nouvelle_province.name = "montant{0}".format(code_p)
            nouvelle_province.save()
        if code_p:
            nouvelle.province = Province.objects.get(code=code_p)

        code_p = fournisseur['pays']
        if code_p and not Pays.objects.filter(code=code_p).exists():
            nouveau_pays = Pays()
            nouveau_pays.code = code_p
            nouveau_pays.name = "montant{0}".format(code_p)
            nouveau_pays.save()
        if code_p:
            nouvelle.pays = Pays.objects.get(code=code_p)

        nouvelle.code_postal = fournisseur['codepostal']
        nouvelle.admissible = fournisseur['admissible']
        nouvelle.conforme = fournisseur['conforme']
        nouvelle.adjudicataire = fournisseur['adjudicataire']
        nouvelle.montant_soumis = fournisseur['montantsoumis']
        
        #Pas encore de fixtures pour les montant soumis
        unite = fournisseur['montantssoumisunite']

        if not UniteMontant.objects.filter(code=unite).exists():
            nouveau_montant = UniteMontant()
            nouveau_montant.code = unite
            nouveau_montant.name = "montant{0}".format(unite)
            nouveau_montant.save()
            
        nouvelle.montant_soumis_unite = UniteMontant.objects.\
                                        get(code=unite)

        nouvelle.montant_contrat = fournisseur['montantcontrat']

        nouvelle.appel = Avis.objects.get(numero_seao=seao)
        nouvelle.save()
