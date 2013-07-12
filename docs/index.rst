.. Django-EpicEd documentation master file, created by
   sphinx-quickstart on Thu Jul 11 21:36:30 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django-EpicEd's documentation!
=========================================

EpicEd is a markdown field with the default widjet using EpicEditor.js
http://epiceditor.com/

This plugin is made to keep a much as possible the possibilities to overide
EpicEditor.js configurations the only settings you'll not be able to edit
are 'container' and 'textarea' since they are rewriten by the wideget and
are needed to save the data to the database.

Contents:

.. toctree::
   :maxdepth: 2

   configurations
   widgetusage


Installing
----------

To install with pip ::

    pip install django-epiceditor

To install from source ::

    git clone https://github.com/belug23/django-epiced.git
    cd django-epiced
    python setup.py install

From source::

    wget https://github.com/belug23/django-epiced/archive/0.2.tar.gz
    tar -zxvf 0.2.tar.gz
    cd django-epiced
    python setup.py install

Using in django
---------------

Add it to your installed apps::

    INSTALLED_APPS = (
        ...
        'epiced',
    )

and then use it to your model::

    from epiced.models import EpicEditorField

    class Post(models.Model):
        article = EpicEditorField()
        ...





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

