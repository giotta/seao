# seao

Exploration des données ouvertes sur les appels d'offres (seao) du Québec

## Licence

La licence de ce logiciel est accessible dans le fichier :
LICENSE.md

## Données

Ce logiciel utilise des données ouvertes mise à disposition par le 
Gouvernement du Québec.

### Source
http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995

Ces données reformattées sont mise à disposition pour la communauté à l'URL :
http://seao.pourvotre.info/avis.json

Ce logiciel utilise directement ces données reformattées.

Aussi, les données sont reliées à des listes de valeurs décrites dans les
spécifications :
http://donnees.gouv.qc.ca/geonetwork/srv/en/resources.get?id=999&fname=SEAO_-_Spcifications_XML_donnes_ouvertes_-_20130418.pdf&access=private

Ce logiciel inclut ces listes de valeurs comme données initiales de références (fixes).
seao_ouvert/api/fixtures/donnees_champs.json

### Licence
http://www.donnees.gouv.qc.ca/?node=/licence

Mention à publier conformément à la licence :
Comprend des données ouvertes octroyées sous la licence d'utilisation des données ouvertes de l’Administration gouvernementale disponible à l'adresse Web : www.données.gouv.qc.ca . L'octroi de la licence n'implique aucune approbation par l'Administration gouvernementale de l'utilisation des données ouvertes qui en est faite.

## Installation
Ce logiciel est codé en Python avec l'aide du framework de développement
web Django. Les autres dépendances logicielles sont déclarées dans
requirements.txt

### Debian/Ubuntu
Pour installer ce logiciel sur distribution Linux basée sur Debian:

<pre>
# cloner le dépôt git
git clone https://github.com/giotta/seao.git

# installation de virtualenv
sudo apt-get install python-virtualenv

# installation des dépendances du projet
cd seao
virtualenv --no-site-packages --distribute env
source env/bin/activate
pip install -r requirements.txt
#pip install django
#pip install south

# création de la base de données locale
python manage.py syncdb --migrate
# créez vous un user admin quand on vous le demande

# charger des données initiales
python manage.py loaddata seao_ouvert/api/fixtures/donnees_champs.json

# récupérer les données seao
# étape facultative car données peuvent être récupérées à distance lors du chargement
# si vous les voulez en local :
# créer un répertoire data/ à la racine des sources du projet
# sauvegarder ce fichier dans le répertoire data"
# http://seao.pourvotre.info/avis.json
# vous devriez alors avoir : data/avis.json

# charger les données seao
python manage.py load_avis
# ou pour fichier local : python manage.py load_avis -f data/avis.json

# lancer le serveur en local
python manage.py runserver
</pre>
