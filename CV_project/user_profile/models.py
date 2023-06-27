from django.db import models

# Create your models here.

class About(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

class Experience(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=200)

class Education(models.Model):
    title = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=200)

class Certifications(models.Model):
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()

class Skills(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()

class Interests(models.Model):
    name = models.CharField(max_length=50)