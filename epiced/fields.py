# -*- coding: utf-8 -*-
from django.db import models
from django import forms

from .widgets import EpicEditorWidget

from markdown import markdown


class EpicEditorField(models.TextField):

    def __init__(self, *args, **kwargs):
        self._markdown_safe = not kwargs.pop('allow_html', True)
        self._html_field_suffix = kwargs.pop('html_field_suffix', '_html')
        self.configs = kwargs.pop("configs", None)
        super(EpicEditorField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        self._html_field = "%s%s" % (name, self._html_field_suffix)
        models.TextField(editable=False).contribute_to_class(
            cls, self._html_field)
        super(EpicEditorField, self).contribute_to_class(cls, name)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        html = markdown(value, safe_mode=self._markdown_safe)
        setattr(model_instance, self._html_field, html)
        return value

    def formfield(self, **kwargs):
        defaults = {
            'form_class': EpicEditorFormField,
            'configs': self.configs,
        }
        defaults.update(kwargs)
        return super(EpicEditorField, self).formfield(**defaults)

    def __unicode__(self):
        return self.attname


class EpicEditorFormField(forms.fields.Field):

    def __init__(self, configs=None, *args, **kwargs):
        kwargs.update({'widget': EpicEditorWidget(configs=configs)})
        super(EpicEditorFormField, self).__init__(*args, **kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^epiced\.fields\.EpicEditorField"])
except:
    pass
