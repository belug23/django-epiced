import json

from django import VERSION as DJANGO_VERSION

from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_text
from django.core.exceptions import ImproperlyConfigured

if DJANGO_VERSION >= (1, 8):
    from django.forms.utils import flatatt
else:  # Django < 1.8 compatibility
    from django.forms.util import flatatt


DEFAULT_EPICEDITOR_CONFIG = {

    "container": 'epiceditor',
    "textarea": None,
    "basePath": settings.STATIC_URL + 'epiced',
    "clientSideStorage": False,
    "localStorageName": 'epiceditor',
    "useNativeFullscreen": True,
    "parser": 'marked',
    "file": {
        "name": 'epiceditor',
        "defaultContent": '',
        "autoSave": 100
    },
    "theme": {
        "base": '/themes/base/epiceditor.css',
        "preview": '/themes/preview/preview-dark.css',
        "editor": '/themes/editor/epic-dark.css'
    },
    "button": {
        "preview": True,
        "fullscreen": True
    },
    "focusOnLoad": True,
    "shortcut": {
        "modifier": 18,
        "fullscreen": 70,
        "preview": 80
    },
    "string": {
        "togglePreview": 'Toggle Preview Mode',
        "toggleEdit": 'Toggle Edit Mode',
        "toggleFullscreen": 'Enter Fullscreen'
    }
}


class EpicEditorWidget(forms.Textarea):

    """
    Widget providing EpicEditor for Markdown Editing.
    """
    class Media:
        try:
            if settings.DEBUG is True:
                js = (
                    settings.STATIC_URL + 'epiced/js/epiceditor.js',
                )
            else:
                js = (
                    settings.STATIC_URL + 'epiced/js/epiceditor.min.js',
                )
        except AttributeError:
            raise ImproperlyConfigured("django-epiced requires \
                    STATIC_URL setting. This setting specifies a \
                    URL prefix to the epiceditor JS and CSS Statics")

    def __init__(self, configs=None, max_length=None, *args, **kwargs):
        super(EpicEditorWidget, self).__init__(*args, **kwargs)
        # Setup config from defaults.
        self.config = DEFAULT_EPICEDITOR_CONFIG.copy()
        self.max_length = max_length

        # Try to get valid config from settings.
        settings_configs = getattr(settings, 'EPICEDITOR_CONFIG', None)
        if settings_configs:
            self.config.update(settings_configs)
        if configs:
            self.config.update(configs)

    def render(self, name, value, attrs={}):

        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)

        self.config['container'] = "%s_epiceditor" % (final_attrs['id'], )
        self.config['textarea'] = final_attrs['id']

        return mark_safe(
            render_to_string('epiced/widget.html', {
                'final_attrs': flatatt(final_attrs),
                'parser': self.config['parser'],
                'field_id': final_attrs['id'],
                'editor_id': final_attrs['id'].replace('-', '_'),
                'value': conditional_escape(force_text(value)),
                'config': json.JSONEncoder().encode(self.config),
                'maxlength': None  # Not supported by EpicEditor: self.max_length
        }))
