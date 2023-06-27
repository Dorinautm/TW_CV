from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Experience, Education, Certifications, Skills, Interests


# Create your views here.
def index(request):
    about_data = About.objects.first()
    experience_data = Experience.objects.all()
    education_data = Education.objects.all()
    certifications_data = Certifications.objects.all()
    skills_data = Skills.objects.all()
    interests_data = Interests.objects.all()

    return render(request, 'index.html', {'cv_data': about_data, 'experience_data':experience_data, 'education_data': education_data, 'certifications_data':certifications_data, 'skills_data': skills_data, 'interests_data':interests_data})
