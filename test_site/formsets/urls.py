# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import formsetView

urlpatterns = patterns('',
    url(r'^$', formsetView.as_view(), name='formsets_test'),
)