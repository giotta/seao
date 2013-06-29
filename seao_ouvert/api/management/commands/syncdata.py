from django.core.management.base import BaseCommand
from seao_ouvert.api.models import *
from optparse import make_option
import datetime, urllib2, HTMLParser
from bs4 import BeautifulSoup
import pdb
from django.utils import timezone


class Command(BaseCommand):

    URL_SEAO = 'http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995'

    option_list = BaseCommand.option_list +  (

        )

    help = BaseCommand.help + "Effectue la synchronisation entre la bd locale et les donnees de seao"

    def handle(self, *args, **options):

        for link in self.file_links():
            self.stdout.write(link)

    def file_links(self):
        '''
        Returns xml files download links
        '''

        page = urllib2.urlopen(self.URL_SEAO).read()
        soup = BeautifulSoup(page)

        links = []

        for a in soup.find_all("img", src="images/download.png"):
            links.append(a.find_parent("a")['href'])

        return links
