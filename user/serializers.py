from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email','name','password']
        
    def create(self, validated_data):
        if validated_data:
            email = validated_data.pop('email')
            password = validated_data.pop('password')
            name = validated_data.pop('name')
            user = User.objects.create_user(email=email,password=password,**validated_data)
            user.name = name
            user.save()
            return user
        
class EmailGetTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        
        email = attrs.get('email')
        password = attrs.get('password')
        
        self.user = authenticate(request=self.context.get('request'), username=email , password=password, backend ='user.backends.UserAuthenticationBackend' )
        if not self.user :
            return serializers.ValidationError((f'No active user found with {email}'),code='authentication')
        
        data ={}
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        return data
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token