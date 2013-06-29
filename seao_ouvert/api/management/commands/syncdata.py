# TODO: clean up the import section.
from django.core.management.base import BaseCommand
from zipfile import ZipFile
from seao_ouvert.api.models import *
from optparse import make_option
import datetime, urllib2
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
        self.extract_files(urls)
        print "--------------------------------"
        print "Call load_xml to rock"
        print "================================"
        print "END of local import of data from source"


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
    
        for url in urls:

            parsed_url = urlparse(url)
            filename = parse_qs(parsed_url.query)['fname'][0]
            
            zip_file_path = "%s%s" % (self.LOCAL_PATH, filename)
    
            with ZipFile(zip_file_path, 'r') as zip_file:
                zip_file.extractall(self.LOCAL_PATH)
    
            print "From :"
            print zip_file_path
            print "Extracting all files to :"
            print "%s" % (self.LOCAL_PATH,)

        if not urls:
            print "No files to extract."
        
