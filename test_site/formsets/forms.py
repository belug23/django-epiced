# -*- coding: utf-8 -*-
from django import forms
from epiced.widgets import EpicEditorWidget


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=EpicEditorWidget())