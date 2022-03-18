from dataclasses import field
from .models import UserProfile,Area
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)
    areaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Area.objects.all(), source='area')
    
    def create(self,validate_data):
        user = UserProfile(**validate_data)
        hashed_pwd = make_password(validate_data['password'])
        user.password = hashed_pwd
        
        user.save()
        return user
    
    def validPassword(password1,password2):
        return check_password(password2,password1)
        
    class Meta:
        model = UserProfile
        fields = ('id','name','password','area','areaId')
