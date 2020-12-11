from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles_images/%Y/%m/%d/')
    company = models.CharField(max_length=100, blank=False)
    website = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=100, blank=False)
    bio = models.CharField(max_length=100, blank=False)
    githubusername = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=100, blank=False)

    experinece_title = models.CharField(max_length=100, blank=True)
    experinece_company = models.CharField(max_length=100, blank=True)
    experinece_location = models.CharField(max_length=100, blank=True)
    experinece_from_date = models.DateTimeField(default=datetime.now, blank=True)
    experinece_to = models.DateTimeField(default=datetime.now, blank=True)
    experinece_current = models.BooleanField(default=False)
    experinece_description = models.CharField(max_length=250, blank=True)

    youtube = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)

    education_school = models.CharField(max_length=100, blank=True)
    education_degree = models.CharField(max_length=100, blank=True)
    education_fieldofstudy = models.CharField(max_length=100, blank=True)
    education_from_date = models.DateTimeField(default=datetime.now, blank=True)
    education_to_date = models.DateTimeField(default=datetime.now, blank=True)
    education_current = models.BooleanField(default=False)
    education_description = models.CharField(max_length=250, blank=True)


    def __str__(self):
        return self.user.username

# A ForeignKey is for one-to-many, so a Car object might have many Wheels, each Wheel having a ForeignKey to the Car it belongs to. A OneToOneField would be like an Engine, where a Car object can have one and only one.