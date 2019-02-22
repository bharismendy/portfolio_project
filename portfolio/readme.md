-----
<div style="text-align:center;">
<h1> Documentation d'installation du portfolio<h1>
</div>

-----------
# Introduction
cette documentation rédigé en markdown a pour but d'expliquer la mise en place du site web


### installation des paquets nécessaire

Voici la commande a exécuter pour installer tout les programmes nécessaire :

      sudo apt-get install virtualenv python3.6 python-mysqldb mysql-server apache2 mysql-client phpmyadmin gcc  python3.6-dev libmysqlclient-dev

Nous créons ensuite l'environement virtuel :

    virtualenv venv -p python3.6

Puis nous installons l'ensemble des paquets :

    configparser==3.5.0
    Django==2.1.2
    django-bootstrap4==0.0.7
    mysqlclient==1.3.13
    pkg-resources==0.0.0
    pytz==2018.5


il nous faut ensuite créer l'utilisateur en base de donnée :
