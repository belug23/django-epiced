.. _about:

About
=====

Installation
------------

To install with pip ::

    pip install django-epiceditor

To install from source ::

    git clone https://github.com/belug23/django-epiced.git
    cd django-epiced
    python setup.py install

From source::

    wget https://github.com/belug23/django-epiced/archive/0.4.3.tar.gz
    tar -zxvf 0.4.3.tar.gz
    cd django-epiced
    python setup.py install

Usage
-----

Add it to your installed apps::

    INSTALLED_APPS = (
        ...
        'epiced',
    )

and then use it to your model::

    from epiced.models import EpicEditorField

    class Post(models.Model):
        ...
        article = EpicEditorField()
        ...

by default the field will escape all the HTML saved, to use it with HTML
you need to add a safe_mode parameter::

    from epiced.models import EpicEditorField

    class Post(models.Model):
        article = EpicEditorField(safe_mode=False)

for more information look at http://pythonhosted.org/Markdown/reference.html#safe_mode
