from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import CreateUser
class UserCreateRetrieveView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateUser
    queryset = User.objects.all()

    def get_permissions(self):
        permissions = []
        if self.action == 'retrieve':
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

