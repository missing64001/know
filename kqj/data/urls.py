from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$',tree_view, name='tree_view'),
    url(r'^tree/$',tree_view, name='tree_view'),
    url(r'^getdata/$',getdata_view, name='getdata_view'),
]