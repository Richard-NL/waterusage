## Run after vagrant up
sudo -u postgres psql postgres
sudo -u postgres createdb waterusage
sudo -u postgres createuser --superuser vagrant

psql -U vagrant -d waterusage
GRANT ALL PRIVILEGES ON DATABASE "waterusage" to vagrant


## To generate sql file
python3 manage.py sqlmigrate water 0001
#python3 manage.py sqlmigrate water 0002
#python3 manage.py sqlmigrate water 0003


## reset db user and password
sudo -u vagrant psql waterusage
ALTER USER "vagrant" WITH PASSWORD 'vagrant';


## create admin user in django (8 char password)
python3 manage.py createsuperuser

## to migrate the db
python3 manage.py migrate


#install django
sudo pip3 install Django
sudo pip3 install psycopg2

## Run the server
python3 manage.py runserver 192.168.192.11:8181


## create migration file
python3 manage.py makemigrations water
