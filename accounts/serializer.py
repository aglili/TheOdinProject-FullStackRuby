from rest_framework import serializers
from .models import CustomUser





class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','password']



    def validate_username(self, value):
        if CustomUser.objects.filter(username=value['username']).exists():
            raise serializers.ValidationError({"error":"Username Already Exists"})
        return value
    
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value['email']).exists():
            raise serializers.ValidationError({"error":"Email Has Already Been Used"})
        return value

    
    def validate(self, data):
        if 'username' in data:
            data['username'] = data['username'].lower()
        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create(first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],username=validated_data['username'],
                                         email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        