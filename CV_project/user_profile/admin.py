from django.contrib import admin
from .models import About, Certifications, Education, Experience, Interests, Skills
# Register your models here.
admin.site.register([About, Experience, Education, Certifications, Skills, Interests])
