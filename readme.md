## Setup django with postgres 
This code is associated with a blog written on medium read the [article](https://gh0stfrk.medium.com/set-up-a-django-application-with-postgres-database-1da6c4ce6b25) to follow along.


## Local development environment 
- Install dependencies 
```
pip install requirements.txt
```
- Change database configuration in [settings.py](./djangowithpostgress/settings.py) file
- Create a database in postgres server
- Create tables in the database with migrations
```
python3 manage.py migrate
```
- Start the development server 
```
python3 manage.py runserver
```
