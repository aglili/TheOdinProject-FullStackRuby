from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email']



    def validate_username(self, value):
        if CustomUser.objects.filter(username=value.lower()).exists():
            raise serializers.ValidationError({"error":"Username Already Exists"})
        return value
    
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError({"error":"Email Has Already Been Used"})
        return value

    
    def validate(self, data):
        if 'username' in data:
            data['username'] = data['username'].lower()
            data['email'] = data['email'].lower()
        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create(first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],username=validated_data['username'],
                                         email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True)

    def validate_username(self, value):
        if not CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError({"error": "Username is incorrect"})
        return value

    def create_token(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        if not user:
            return {"error": "Invalid credentials", "data": {}}
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': "Login successful"
        }

