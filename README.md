# Ecommerce Website Development using Django on a Docker Container.

# Please Install Docker, Docker-compose, Python 3 and Pip, Tmux before doing anything of the commands below in the directory,

- pip install -r requirements.txt
## Starting up the server
- docker-compose up -d
- Website will be avalible at http://localhost:8080/

**When you start Running the File.
Do not run docker-compose up -d and docker-compose up at the same time. That will wipe out the DataBase as you replace the memory by reininitializing the container.
Just Run either one and if you run docker-compose up -d remember to run docker-compose down after you're done using the container.

# if you're running AWS ubuntu please run the following command to get be set up.
- bash bash.txt

## The following is a cheat
# Docker Commnads

To Shut down your Docker Image enter the following command.

- docker-compose down

Make Migrations using these commands.

- docker-compose exec web python /code/ecommerce/manage.py makemigrations
- docker-compose exec web python /code/ecommerce/manage.py migrate

Create new user if You can't log in.

- docker-compose exec web python /code/ecommerce/manage.py createsuperuser
- docker rmi \$(docker images -a -q) | Remove current Images
- docker-compose up

# Tmux Commands
- CTRL-B % [To open a new window]
- CTRL-B c [To create a new tab]

# SuperUser Credentials for now

- Username: Admin
- Password: password

# remove cache

- rm -rf ecommerce/ecommerce/**pycache**

