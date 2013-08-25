from django.db import models
from epiced.models import EpicEditorField


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = EpicEditorField(html_field_suffix='_test')
    article = EpicEditorField(safe_mode=False)

    def __unicode__(self):
        return self.title

