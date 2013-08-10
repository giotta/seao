# coding: utf-8

import urllib2
from zipfile import ZipFile

from seao_ouvert.api import models as api


SOURCE_URL = "http://http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995"
SOURCE_DOWNLOAD_URL = "http://donnees.gouv.qc.ca/geonetwork/srv/en/resources.get?id=999&access=private&fname="
SOURCE_FILES = []

LOCAL_PATH = "../../data/"
LOCAL_FILES = []


def get_files_from_source():
    print "Finding data files from source :"

    # TODO : code logic
    # pour une date de début...
    # ... rechercher fichiers égaux ou plus grands que date début
    findings = ['Avis_20130501_20130531.zip',]
    for file in findings:
        SOURCE_FILES.append(file)

    print "From :"
    print SOURCE_URL
    print "Founded :"
    for file in SOURCE_FILES:
        print "* %s" % (file,)

def download_files():
    print "Downloading data files from source :"

    for file in SOURCE_FILES:
        source_path = "%s%s" % (SOURCE_DOWNLOAD_URL, file,)
        local_path = "%s%s" % (LOCAL_PATH, file,)

        zip_file = urllib2.urlopen(source_path)
        
        with open(local_path,'wb') as f: f.write(zip_file.read())

        LOCAL_FILES.append(file)

        print "From :"
        print source_path
        print "Download to :"
        print local_path

def extract_data():
    print "Extracting data from local files :"

    for file in LOCAL_FILES:
        zip_file_path = "%s%s" % (LOCAL_PATH, file)

        with ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(LOCAL_PATH)

        print "From :"
        print zip_file_path
        print "Extracting all files to :"
        print "%s" % (LOCAL_PATH,)

if __name__ == "__main__":
    print "SEAO Ouvert"
    print "START import of data from source to local"
    print "================================"
    get_files_from_source()
    print "--------------------------------"
    download_files()
    print "--------------------------------"
    extract_data()
    print "--------------------------------"
    print "Call load_xml to rock"
    print "================================"
    print "END of local import of data from source"
