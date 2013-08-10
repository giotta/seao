# SEAO Ouvert

Exploration des données ouvertes sur les appels d'offres (seao) du Québec

## Licence

La licence de SEAO Ouvert est accessible dans le fichier :
LICENSE.md

## Données

SEAO Ouvert utilise des données ouvertes mises à disposition par le 
Gouvernement du Québec.

### Source
http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995

Ces données reformattées sont mises à la disposition de la communauté à l'URL :
http://seao.pourvotre.info/avis.json

Aussi, les données sont reliées à des listes de valeurs décrites dans les
spécifications :
http://donnees.gouv.qc.ca/geonetwork/srv/en/resources.get?id=999&fname=SEAO_-_Spcifications_XML_donnes_ouvertes_-_20130418.pdf&access=private

SEAO Ouvert inclut ces listes de valeurs comme données initiales de références (fixes).
seao_ouvert/api/fixtures/donnees_champs.json

### Licence
Les informations de licence relatives aux données de SEAO Ouvert se trouvent dans ce fichier :
LICENSE.md

## Installation
SEAO Ouvert est codé en Python avec l'aide du framework de développement
web Django. Les autres dépendances logicielles sont déclarées dans
requirements.txt

### Debian/Ubuntu
Pour installer SEAO Ouvert sur une distribution Linux basée sur Debian:

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

# création de la base de données locale
python manage.py syncdb --migrate
# créez vous un user admin quand on vous le demande

# charger des données initiales
python manage.py loaddata seao_ouvert/api/fixtures/donnees_champs.json

# charger les données seao
# l'opération peut prendre du temps, 
# démarrez votre télésérie préférée.
python manage.py syncdata

# lancer le serveur en local
python manage.py runserver
</pre>
