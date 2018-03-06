from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from django.contrib import admin

urlpatterns = [
    #Do not do this in your projects, this is only for the test, do it in views
    url(r'^$', TemplateView.as_view(template_name='testindex.html'), name='index'),

    url(r'^formsets/', include('formsets.urls', namespace="formsets")),
    url(r'^testadmin/', include('testadmin.urls', namespace="testadmin")),
    url(r'^admin/', include(admin.site.urls)),
]
