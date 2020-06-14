# Todo API
An API for creating, updating, retrieving and deleting todo tasks.

## How to install
+ create a virtualenv and activate it
+ install required modules
+ set environment variables
+ create and migrate database
+ run application

#### Create a virtualenv and Activate it
Assuming windows:

~~~
virtualenv venv
cd venv/scripts
activate
~~~

### Install required modules
~~~
pip install -r requirements.txt
~~~

### set environment variables
Assuming windows:

~~~
set FLASK_ENV=development
set FLASK_APP=todo:factory
~~~

### Create and migrate database
~~~
flask db init
flask db migrate
flask db upgrade
~~~

### Run application
~~~
flask run
~~~

The development server is run at localhost:5000

# Documentation
+ POST
Example Request  
curl --location --request POST 'http://localhost:5000/api/v1/?task=Cook%20Rice&description=Cook%20Rice%20for%20lunch%20by%202pm'  

+ PUT
Example Request
curl --location --request PUT 'http://localhost:5000/api/v1/1?task=Cook%20Rice&description=Cook%20Rice%20for%20lunch%20by%201pm'  

+ GET
Example Request
curl --location --request GET 'localhost:5000/api/v1/1'  

+ GET
Example Request
curl --location --request GET 'localhost:5000/api/v1/'  

+ DELETE
curl --location --request DELETE 'localhost:5000/api/v1/'
