from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$',tree_view, name='tree_view'),
    url(r'^tree/$',tree_view, name='tree_view'),
    url(r'^getdata/$',getdata_view, name='getdata_view'),
    url(r'^xs/$',xs_view, name='xs_view'),
    url(r'^getxsdata$',getxsdata_view, name='getxsdata_view'),
    url(r'^asset$',asset_view, name='asset_view'),

]