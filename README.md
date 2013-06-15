# seao

Exploration des données ouvertes sur les appels d'offres (seao) du Québec

## Licence

La licence de ce logiciel est accessible dans le fichier :
LICENSE

## Données

Ce logiciel utilise des données ouvertes mise à disposition par le 
Gouvernement du Québec.

### Source
http://www.donnees.gouv.qc.ca/?node=/donnees-details&id=542483bf-3ea2-4074-b33c-34828f783995

### Licence
http://www.donnees.gouv.qc.ca/?node=/licence

Mention à publier conformément à la licence :
Comprend des données ouvertes octroyées sous la licence d'utilisation des données ouvertes de l’Administration gouvernementale disponible à l'adresse Web : www.données.gouv.qc.ca . L'octroi de la licence n'implique aucune approbation par l'Administration gouvernementale de l'utilisation des données ouvertes qui en est faite.

## Installation
Ce logiciel est codé en Python avec l'aide de le framework de développement
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
pip install django
pip install south

# création de la base de données locale
python manage.py syncdb --migrate

# lancer le serveur en local
python manage.py runserver
</pre>
