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
+ POST add todo 1  
http://localhost:5000/api/v1/?task=Cook Rice&description=Cook Rice for lunch by 2pm  
method: Post  
Param:
+ task: short description
+ description: long description
Add a todo object to the database.

Example Request  
curl --location --request POST 'http://localhost:5000/api/v1/?task=Cook%20Rice&description=Cook%20Rice%20for%20lunch%20by%202pm'  

+ POST add todo 2  
http://localhost:5000/api/v1/?task=Laundry&description=Do laundry by 10pm before sleeping  
method: Post  
Param:  
+ task: short description
+ description: long description
Add a todo object to the database.

Example Request  
curl --location --request POST 'http://localhost:5000/api/v1/?task=Laundry&description=Do%20laundry%20by%2010pm%20before%20sleeping'  

+ POST add todo 3
http://localhost:5000/api/v1/?task=Buy food Items&description=Buy food items from supermarket by 3pm  
method: Post  
Param:
+ task: short description
+ description: long description
Add a todo object to the database.

Example Request
curl --location --request POST 'http://localhost:5000/api/v1/?task=Buy%20food%20Items&description=Buy%20food%20items%20from%20supermarket%20by%203pm'

+ PUT update todo
http://localhost:5000/api/v1/1?task=Cook Rice&description=Cook Rice for lunch by 1pm  
method: Put  
Param:
+ task: short description
+ description: long description
Update todo with id object in the database.

Example Request
curl --location --request PUT 'http://localhost:5000/api/v1/1?task=Cook%20Rice&description=Cook%20Rice%20for%20lunch%20by%201pm'  

+ GET get todo
localhost:5000/api/v1/1
method: Get
Return todo object with id from database

Example Request
curl --location --request GET 'localhost:5000/api/v1/1'  

+ GET get todo list
localhost:5000/api/v1/
method: Get
Return list of all todo in database.

Example Request
curl --location --request GET 'localhost:5000/api/v1/'  

+ GET delete todo
method: Delete
Delete todo with id from database.
