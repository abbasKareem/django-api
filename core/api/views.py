from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer
from api import permissions


class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated, permissions.UpdateOwnProfile]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
        
