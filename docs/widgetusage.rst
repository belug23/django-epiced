.. _widget-usage:

Widget Usage
============

Insted of using the EpicEditorField you can go the hard way by using TextField
and applying the widget directly ::

        from django import forms
        from epiced.widgets import EpicEditorWidget

        class FlatPageForm(forms.ModelForm):
            ...
            content = forms.CharField(widget=EpicEditorWidget())
            ...

You don't forget that you can overwrite the configs directly from the widget ::

        from django import forms
        from epiced.widgets import EpicEditorWidget

        class FlatPageForm(forms.ModelForm):
            ...
            content = forms.CharField(widget=EpicEditorWidget(configs={"focusOnLoad": False}))
            ...

you also need to add the JS::

        <script src="{% static 'epiced/js/epiceditor.js' %}"></script>