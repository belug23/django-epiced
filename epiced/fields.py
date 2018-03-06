# -*- coding: utf-8 -*-
import logging

from django.db import models
from django import forms

from markdown import markdown

from .widgets import EpicEditorWidget

logger = logging.getLogger(__name__)


class EpicEditorField(models.TextField):

    def __init__(self, *args, **kwargs):
        allow_html = not kwargs.pop('allow_html', False)
        safe_mode = kwargs.pop('safe_mode', 'escape')
        if allow_html is not True:
            self._markdown_safe = allow_html
            logger.warning('''The EpicEditorField parameter allow_html\
            is now deprecated due to security problems. Please \
            replace it by safe_mode. Read the\
            documentation for more information''')
        else:
            self._markdown_safe = safe_mode
        self._html_field_suffix = kwargs.pop('html_field_suffix', '_html')
        self.configs = kwargs.pop("configs", None)
        super(EpicEditorField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(EpicEditorField, self).deconstruct()
        path = 'django.db.models.TextField'
        return name, path, args, kwargs

    def contribute_to_class(self, cls, name):
        self._html_field = "%s%s" % (name, self._html_field_suffix)  # noqa
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
        # Support for the max_length option Django 1.7
        max_length = kwargs.pop('max_length', None)
        kwargs.update({'widget': EpicEditorWidget(configs=configs, max_length=max_length)})
        super(EpicEditorFormField, self).__init__(*args, **kwargs)
