from rest_framework import serializers

from users.models import User

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'username', 'email', 'password', 'avatar']
        read_only_fields = ['uid', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
