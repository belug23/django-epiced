.. _configurations:

Configurations
==============

To know the option please visite http://epiceditor.com/#options

There is only two options you can't edit ::

container::

    It's setted to the ID of the field so you can use it on multiple fields in the same time.

textarea::

    It's used with the ID to synchronize automatically multipls fields

Default Settings
----------------

Those are the settings used by default::

    DEFAULT_EPICEDITOR_CONFIG = {
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

Overwriting the Settings
-------------------------

You can partially overwrite the config by adding EPICEDITOR_CONFIGS
your settings.py::

    EPICEDITOR_CONFIG = {
        "basePath": settings.STATIC_URL + 'personal',
        "button": {
            "preview": True,
            "fullscreen": True
        },
    }

You can also do it by using adding a "configs" parameter to your widget or
EpicEditorField::

    text = EpicEditorField(configs={"focusOnLoad": False})

    content = forms.CharField(widget=EpicEditorWidget(configs={"focusOnLoad": False}))
