
# Farm Project - Backend


## Requirements

 - Python 3.5
 - Virtual Enviroment
 - Postgres 
 - Django
 
## RUN

First, clone the repository:
```shell
$ git clone https://bitbucket.org/agrosatelite/farm-project.git
```

After, you need to create your virtual enviroment. You can create using Virtualenv (apt install virtualenv):
```shell
$ virtualenv env -p python3
$ source env/bin/activate
```

Upgrade pip and setuptools

```shell
$ pip3 install --upgrade pip
$ pip3 install setuptools --upgrade
```

Inside the project directory, run the command to install the env requirements:
```shell
$ pip3 install -r requirements.txt
```

### Install PostgreSQL and PostGIS

```shell
$ sudo apt-get install postgresql-client
```

### Install GDAL development libraries:

Go to the root directory of this project locate gdal.sh and execute it with sudoer permission.

```shell
sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libgdal-dev
sudo apt-get install python3-dev
sudo apt-get install gdal-bin python3-gdal
pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

Create a local database name 'farm-project' in the postgres with your user and password.

Inside the farm-project folder create a new file called *local_settings.py*:
```shell
$ touch farm_project/local_settings.py
```

Inside the file *local_settings.py* configure your database, bellow is a template:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'farm-project',
        'USER': 'your-user',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
    }
}

DEBUG =  True
```


Create extensions:

```
$ psql -U your-user -W -h localhost farm-project

$ CREATE EXTENSION postgis;
```

Run the migrations:
```shell
$ python3 manage.py makemigrations 
$ python3 manage.py migrate
```

Create your Django User:
```shell
$ python manage.py createsuperuser
```
Start the application:
```shell
$ python manage.py runserver
```
Look the swagger accessing *http://localhost:8000*
Look the django-admin accessing *http://localhost:8000/admin* and use your superuser email and password.

--- 
# Complete the Farm Project
#####1. Add in the FARM model the following fields:
- Municipality
- State
- A relation between FARM and OWNER (one farm has to have only one owner and the onwer can have zero or many farms).

#####2. Do not allow create farms:
- Without Owner
- Without Geometry
- Without Municipality
- Without State
- Without Name

#####3. Allow search farm by:
- Owner name
- Owner document
- Farm name
- Municipality 
- State 
- ID

#####4. The GET (details) of FARM has to return:
- All fields of the model

#####5. The GET (list) of FARM has to return:
- Name, owner id, centroid, area, municipality and state

## Hints
1. To test your code you can use the swagger to make the requests
2. To test geometry fields you can pass a geojson data, this can be create on *[http://geojson.io/](http://geojson.io/)*  (using just the geometry field in the geojson).
