__author__ = 'Akash'
from django.conf.urls import url
from . import views

urlpatterns = [url(r'^results',views.index,name='index'),
    url(r'^$',views.index2,name='index2')]