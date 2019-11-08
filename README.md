# Ecommerce_repo

#Please Install Docker, Python 3 and Pip before doing anything of the commands below in the directory.

- pip install -r requirements.txt
  Starting up the server
- docker-compose up -d
- Website will be avalible at http://localhost:8000/

  To Shut down your Docker Image enter the following command.

- docker-compose down

Make Migrations using these commands.

- docker-compose exec web python /code/ecommerce/manage.py makemigrations
- docker-compose exec web python /code/ecommerce/manage.py migrate

## some other stuff
