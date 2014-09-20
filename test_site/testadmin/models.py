from django.db import models
from epiced.models import EpicEditorField


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = EpicEditorField(html_field_suffix='_test')
    article = EpicEditorField(safe_mode=False)
    limited= EpicEditorField(safe_mode=False, max_length=30)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

