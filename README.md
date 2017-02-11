docker-compose up
docker exec -it waterusage_django-waterusage_1  bash

python3 manage.py migrate

python3 manage.py createsuperuser
