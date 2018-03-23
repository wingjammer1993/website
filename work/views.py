from django.shortcuts import render
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from work.models import Experience
# Create your views here.

def experience(request):
	posts = Experience.objects.all()
	return render(request, 'work/experience.html', {'object_list': posts})



