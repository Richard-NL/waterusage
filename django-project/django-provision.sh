#!/bin/bash

sudo locale-gen en_US en_US.UTF-8 nl_NL.UTF-8
sudo dpkg-reconfigure locales


sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get -y update
sudo apt-get -y install python3.5
sudo apt-get -y install python3-pip


#install django
sudo pip3 install Django
sudo pip3 install psycopg2

# npm install
curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh

source ~/.profile


mkdir -p /home/vagrant/workspace
/static
sudo chown -R vagrant:vagrant /home/vagrant

sudo apt-get -y install libpq-dev

sudo apt-get -y install postgresql-client
sudo apt-get -y install postgresql postgresql-contrib

sudo apt-get -y install sqlite3 libsqlite3-dev
#sudo -u postgres psql postgres
#sudo -u postgres createdb waterusage
#sudo -u postgres createuser --superuser vagrant



