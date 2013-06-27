# coding: utf-8

import json
from seao_ouvert.api import models as api


SOURCE_URL = "http://http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995"
SOURCE_DOWNLOAD_URL = "http://donnees.gouv.qc.ca/geonetwork/srv/en/resources.get?id=999&access=private&fname="
SOURCE_FILES = []

LOCAL_PATH = "data/"
LOCAL_FILES = []
LOCAL_DATA_XML = []
LOCAL_DATA_JSON = []

def get_files_from_source():
    print "Finding data files from source :"

    # TODO : code logic
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
        # TODO : code logic
        LOCAL_FILES.append(file)
        print "From :"
        print "%s%s" % (SOURCE_DOWNLOAD_URL, file,)
        print "Download to :"
        print "%s%s" % (LOCAL_PATH, file,)

def extract_data():
    print "Extracting data from local files :"

    for zip_file in LOCAL_FILES:
        # TODO : code logic
        xml_file = zip_file + ".xml"
        LOCAL_DATA_XML.append(xml_file)
        print "From :"
        print "%s%s" % (LOCAL_PATH, zip_file)
        print "Extracting to :"
        print "%s%s" % (LOCAL_PATH, xml_file)

def convert_data_in_json():
    print "Converting local data from XML to JSON format :"
    for xml_file in LOCAL_DATA_XML:
        # TODO : code logic
        json_file = xml_file + ".json"
        LOCAL_DATA_JSON.append(json_file)
        print "From :"
        print "%s%s" % (LOCAL_PATH, xml_file)
        print "Converting to :"
        print "%s%s" % (LOCAL_PATH, json_file)

def create_objects():
    print "Creating local objects from local JSON :"
    # TODO ; code logic
    for file in LOCAL_DATA_JSON:
        #avis = json.loads(file)
        print file

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
    convert_data_in_json()
    print "--------------------------------"
    LOCAL_DATA_JSON.append('avis.json')  # TODO : temporary hack
    create_objects()
    print "================================"
    print "END of local import of data from source"
