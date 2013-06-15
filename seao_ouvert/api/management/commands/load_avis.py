from django.core.management.base import BaseCommand
from seao_ouvert.api.models import *
from optparse import make_option

class Command(BaseCommand):

    URL_AVIS = "seao.pourvotre.info/avis.json"

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
            pass
            #load from file
        else:
            pass
            #load from url
