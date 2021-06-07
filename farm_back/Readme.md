
# Farm Project - Backend


## Requirements

 - Python 3.5
 - Virtual Enviroment
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

### Install Spatialite

```shell
$ sudo apt-get install libsqlite3-mod-spatialite
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

1. Add the following fields to the FARM model:
    * Municipality
    * State
    * A relation between FARM and OWNER (one farm needs to have one and only one owner. The owner can have zero or many farms).

2. Add restrictions so that it is not possible to create farms:
    * Without owner
    * Without geometry
    * Without municipality
    * Without state
    * Without name

3. Make it possible to search a farm by:
    * The owner's name
    * The owner's document number/identification
    * The farm's name
    * Municipality 
    * State 
    * The ID of the farm.

4. Edit the GET (details) of FARM so that it returns:
    * All fields of the model

5. Edit the GET (list) of FARM so that it returns:
    * Name, owner id, centroid, area, municipality and state

## Hints
1. To test your code you can use the swagger to make requests
2. To test geometry fields you can pass geojson data. You can create geojson data on *[http://geojson.io/](http://geojson.io/)*  (using just the geometry field in the geojson).
