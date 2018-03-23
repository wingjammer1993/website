from django.shortcuts import render
from education.models import Education
# Create your views here.


def education(request):
	posts = Education.objects.all()
	return render(request, 'education/education.html', {'object_list': posts})



