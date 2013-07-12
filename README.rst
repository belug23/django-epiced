======
EpicEd
======

EpicEd is a markdown field with the default widjet using EpicEditor.js
http://epiceditor.com/

This plugin is made to keep a much as possible the possibilities to overide
EpicEditor.js configurations the only settings you'll not be able to edit
are 'container' and 'textarea' since they are rewriten by the wideget and
are needed to save the data to the database.


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

    OR with south ::

    python manage.py schemamigration ...

5. Create an admin page or a form template.

6. Now you should have the EpicEditor in your admin and/or template.

7. To display the html version of the text in your template use ::

    {{ post.article_html|safe }}

8. Enjoy a markdown editor that won't break your html!


Thanks
------

I'd like to thank Oscar Godson and John Donahue for EpicEditor : http://epiceditor.com/

Thanks to carljm creator of this snippet : http://djangosnippets.org/snippets/882/ used to complete the EpicEditorField

and Shaun Sephton for creating the django-ckeditor that inspired the widget associated with the field https://github.com/shaunsephton/django-ckeditor



