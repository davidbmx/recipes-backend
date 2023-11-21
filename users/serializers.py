from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'username', 'email', 'password', 'avatar']
        read_only_fields = ['uid', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data['user'] = CreateUser(self.user).data
        return data
