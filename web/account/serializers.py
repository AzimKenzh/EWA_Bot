from rest_framework import serializers

from account.models import MyUser, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'status')

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        status = validated_data.get('status')
        user = MyUser.objects.create_user(username=username, status=status, password=password)
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