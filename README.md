## WakoniZone


## Author: [Maureen Njunge](https://github.com/MugureNjunge)

## Description
This application enables a user to connect with other members of his/her neighbourhood.A community memeber is abe to sign up/ in and choose their neighbourhood then get updates on events as well as business updates.




## Technology Used

![](https://img.shields.io/badge/Code-bootstrap-informational?style=flat&logo=bootstrap&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-django-informational?style=flat&logo=django&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-postgress-informational?style=flat&logo=postgress&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-django-rest-framework-informational?style=flat&logo=javascript&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-HTML5-informational?style=flat&logo=html5&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-python-informational?style=flat&logo=python&logoColor=white&color=brightgreen)
![](https://img.shields.io/badge/Code-JavaScript-informational?style=flat&logo=javascript&logoColor=white&color=brightgreen)



## User Stories

Users would like to:
* Sign in with the application to start using.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete hoods and posts.
* Delete hoods,posts,businesses
* Manage the application images and profiles.


## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the home page  | User joins wakonizone | Directed to the home page | 
If user has no account, they click on `Join locality` | User redirected to 'register'  | User then taps on profile to set up profile page |
|Click `Join locality` |You'll be able to get in to that hood| 
| Click `add post` | You'll be able to add a post in that hood| 
| Click `add business` | You'll be able to add a business in that hood| 
| Click `search business` | You'll be able to search business| 

## SetUp / Installation Requirements
## Prerequisites
* python3
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/gladys-gg/neighborhood.git
        $ cd mtaani

## Running the Application
* Creating the virtual environment

        $ python3 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3 manage.py test

This application is developed using: 
[Python3](https://www.python.org/doc/), 
[Django](https://www.djangoproject.com/), 
[HTML](https://getbootstrap.com/) 
[Bootstrap](https://getbootstrap.com/)

## License

Copyright (c) 2022 Mugure Njunge

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
