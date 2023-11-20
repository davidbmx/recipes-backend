from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializers import CreateUser
class UserCreateRetrieveView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateUser
    queryset = User.objects.all()

    def get_permissions(self):
        permissions = []
        if self.action in ['retrieve', 'my_profile']:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
    
    @action(detail=False, methods=['GET'])
    def my_profile(self, request):
        serializer = self.get_serializer_class()
        user_serializer = serializer(request.user, many=False)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    

