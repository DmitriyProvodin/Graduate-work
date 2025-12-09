from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','role')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password','role')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data.get('email',''), role=validated_data.get('role','student'))
        user.set_password(validated_data['password'])
        user.save()
        return user
