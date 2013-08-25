# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import PostListView

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post_list_test'),
)