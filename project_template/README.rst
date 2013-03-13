=============================================
Welcome to the {{ project_name }} project
=============================================

This project uses Django 1.5.

Locations of important files:

* ``chronicle/`` Django project and apps
* ``docs/`` - project documentation (Sphinx)
* ``requirements.txt`` and ``requirements-dev.txt`` - project dependencies
* ``static/`` - static media
* ``templates/`` - project HTML templates

Getting Started
-----------------

The following will help you get a development environment up and running::

    ?> virtualenv --distribute --python=python2.7 chronicle_env
    ?> cd {{ project_name }}_env
    ?> git clone git@github.com:Threespot/{{ project_name }}.git
    ?> source ../bin/activate
    ?> pip install -r {{project_name }}/requirements.txt
    ?> pip install -r {{ project_name }}/requirements-dev.txt
    ?> cd {{ project_name }}
    ?> ./manage.py syncdb
    ?> ./manage.py runserver
