I am learning various technologies and at the same time working on project.

Technology Used
- Tailwind CSS
- Vue.js
- GraphQL
- Django


Setup of django and its virtual environment
- Install python
- Install pip3 (which is latest version for python package manager )
- Install new python virtual environment
    python3 -m venv env
- Activate virtual environment
    source env/bin/activate
        or
    env/Scripts/activate (if WSL is used)
- Create django project
    python -m pip install Django
    django-admin startproject backend
    python manage.py startapp blog

Seeding data to django application
- Install package named 
    https://pypi.org/project/django-seeding/
- This package require 
    pip3 install pandas (https://pypi.org/project/django-pandas/)
    pip install djangorestframework (https://pypi.org/project/djangorestframework/)

