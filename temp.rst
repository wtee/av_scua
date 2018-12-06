=======================
Temporary Instructions
=======================

-------------
Overview
-------------
This file will document how I build SUCA's AV Database. I will be using a
2NF database, js datatables, django admin, bootstrap. This also needs the ability
to search and export a csv file.

.. code:: shell

  django-admin startproject AV_SCUA
  cd AV_SCUA
  django-admin startapp basic

1. Add TEMPLATES_DIR and add app to settings.py
2. set up first test
3. first test passes by adding templates/basic/home.html, basic/urls.py, urls.py,
and creating a simple view in basic/views.py

#################
Functional Test
#################

Functional test boots up a live server and checks if layout is correct.
This makes use of selenium.

.. code:: shell

  pip install selenium

To run all tests, use

.. code:: shell

  python manage.py test


#####################
Create Super User
#####################
.. code:: shell

  python manage.py makemigrations
  python manage.py migrate

Creating superuser with name and password

.. code:: shell

  python manage.py createsuperuser
