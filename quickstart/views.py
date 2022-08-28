
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows users to be viewed or edited
    """
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]