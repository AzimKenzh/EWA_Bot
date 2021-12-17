from rest_framework import serializers

from account.models import MyUser
from parsing.models import ImportExcels


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password')

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(username=username, password=password)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=130)
    password = serializers.CharField()

    class Meta:
        fields = ('username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username')