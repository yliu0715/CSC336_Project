sudo docker-compose run app sh -c "python manage.py makemigrations core"
sudo docker-compose run app sh -c "python manage.py migrate"
clear
sudo docker-compose run app sh -c "python manage.py runserver"