from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ReadUserSerializer, WriteUserSerializer
from django.core.exceptions import PermissionDenied


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WriteUserSerializer
        else:
            return ReadUserSerializer

    permission_classes = [permissions.AllowAny]


def get_user_id(request):
    if request.user.is_authenticated:
        return request.user.id
    else:
        raise PermissionDenied()