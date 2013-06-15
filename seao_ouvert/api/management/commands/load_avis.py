from django.core.management.base import BaseCommand
from models import *

class Command(BaseCommand):

    URL_AVIS = "seao.pourvotre.info/avis.json"

    parser.add_option("-f", "--fichier", action="store",\
                      type="string", dest="fichier", default=None)

    help = BaseCommand.help + "Load les donnees des avis a partir dun fichier json"

    def handle(self, *args, **options):
        pass
