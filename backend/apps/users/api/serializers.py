from rest_framework import serializers
from apps.users.services import create_user
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        
    def create(self, validated_data):
        return create_user(**validated_data)