# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import formsetView

urlpatterns = [
    url(r'^$', formsetView.as_view(), name='formsets_test'),
]
