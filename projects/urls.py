from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project, name='projects'),
    ]