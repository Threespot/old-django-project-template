#############################################
Threespot Django Project Bootstrapping
#############################################

What is this?
===============

This is a project template for Django 1.5.X. It should be used whenever a new Django project is started to ensure the consistency of all of Threespot's Django project layouts. It also provides lots of useful features which will get development up and running more quickly.

What's in it?
===================

* A basic folder structure for templates, uploaded media and static files
* Stub requirements files for the project and for developers
* The admin (with password reset capabilities) and admindocs apps are already enabled
* A stubbed-out `Sphinx <http://sphinx.pocoo.org/>`_ documentation directory with a working `autodoc <http://sphinx.pocoo.org/tutorial.html#autodoc>`_ configuration.
* A method of versioning settings by development, staging, and production environments; a way of locally overriding settings; sane settings defaults.

What's *not* in it?
===================

* Initial static files (like ``jquery.js`` or any ``reset.css`` files)
* Any template structure  beyond a ``base.html`` template
* Apps
* Documentation for your apps

How do I use it?
===================

Clone the repo from github::

    ?> git clone git@github.com:Threespot/django-project-template.git

Then run the ``startproject`` command with the following arguments::

    ?> django-admin.py startproject myproject --template=django-project-template/project_template/ --extension=py,rst,html,txt

And that's it! You should now have a directory called ``myproject`` that is a fully-bootstrapped Django project.
