# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list_test'),
]
