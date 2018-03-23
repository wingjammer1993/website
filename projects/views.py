from django.shortcuts import render
from projects.models import Project
# Create your views here.


def project(request):
	posts = Project.objects.all()
	return render(request, 'projects/project.html', {'object_list': posts})