======
EpicEd
======

EpicEd is a markdown field with the default widjet using EpicEditor.js
http://epiceditor.com/

This plugin is made to keep a much as possible the possibilities to overide
EpicEditor.js configurations the only settings you'll not be able to edit
are 'container' and 'textarea' since they are rewriten by the wideget and
are needed to save the data to the database.

Warning
-------

Since Version 0.3.0 the html escaping of in markdown is now at true by default.
If you want to add HTML tags in your content add 'safe_mode=False' in the field
options. **PLEASE becareful** with that, do not disable html escaping in public
fields.

Quick start
-----------

1. Install django-epiced ::

    pip install django-epiced

2. Add it to your installed apps ::

    INSTALLED_APPS = (
        ...
        'epiced',
    )

3. Use it in your model ::

    from epiced.models import EpicEditorField

    class Post(models.Model):
        article = EpicEditorField()

4. Sync your database ::

    python manage.py syncdb

5. Create an admin page or a form template.

6. Now you should have the EpicEditor in your admin and/or template.

7. To display the html version of the text in your template use ::

    {{ post.article_html|safe }}

8. Enjoy a markdown editor that won't break your html!


Form more read the documentation at : http://django-epiced.readthedocs.org

Thanks
------

I'd like to thank John Gruber and Aaron Swartz.for the markdown language
http://daringfireball.net/projects/markdown/

Thanks to Oscar Godson and John Donahue for EpicEditor : http://epiceditor.com/

Thanks to carljm creator of this snippet :
http://djangosnippets.org/snippets/882/ used to complete the EpicEditorField

and Shaun Sephton for creating the django-ckeditor that inspired the widget
associated with the field https://github.com/shaunsephton/django-ckeditor

History
-------

*0.4.3* ::
 
    - Updated support to Django 1.11
    
*0.4.2* ::
 
    - Fixed issue #10 A leftover debugging print

*0.4.1* ::
 
    - Fixed issue #9 that would prevent the settings config to override the default config

*0.4.0* ::
 
    - Added support for Django 1.7
    - Added support for Django 1.7 Migrations (Ugly patch)
    - Added support for Python 3

*0.3.1* ::

    - Updated to Epic Editor 0.2.2

*0.3.0* ::

    *Warning, since it's so easy to use this pluggin I've changed the default
    escaping of the HTML, Please refer to the documentation.*
    - Security update : now html is escaped by default
    - Added the automatic install of Markdown (Thanks daikeren for the patch)
    - Added formsets support (Thanks szuliq for the bug repport)
    - Added small test_site for debugging
    - Updated documentation for the security update

*0.2.1* ::

    Typo correction in the documentation

*0.2.0* ::

    bug fixes: Double slashes in images url
    Typos


*0.1.0* ::

    First Release

.. image:: https://cruel-carlota.pagodabox.com/3b76f31ab8defaf2e21114eb1575a220
    :alt: githalytics.com
    :target: http://githalytics.com/belug23/django-epiced
