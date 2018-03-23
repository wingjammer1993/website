from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from work.models import Experience
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.education, name='education'),

]