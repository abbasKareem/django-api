from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


        # ['user', 'profile_image', 'company', 'website', 'location', 'status', 'bio', 'githubusername', 'skills', 'experinece_title', 'experinece_company', 'youtube', 'education_school']