from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import CreateUser, CustomTokenObtainPairSerializer
class UserCreateRetrieveView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateUser
    queryset = User.objects.all()

    def get_permissions(self):
        permissions = []
        if self.action in ['retrieve', 'my_profile']:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'ssession': {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
        }, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['GET'])
    def my_profile(self, request):
        serializer = self.get_serializer_class()
        user_serializer = serializer(request.user, many=False)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data['refresh']
        access = response.data['access']
        user = response.data['user']

        return Response({
            'user': user,
            'session': {
                'access': access,
                'refresh': refresh,
            }
        })

