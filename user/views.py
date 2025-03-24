from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterUserSerializer,EmailGetTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class RegisterUserView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self,request):
        
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        
        if user:
            return Response({'message':'user is already register!!!'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            serializer = RegisterUserSerializer(data = request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({'message':'user registered lets move to more details now!!!'},status=status.HTTP_201_CREATED)
            
            return Response({'message':'Oops something went wrong with serializer !!!'},status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
class GetEmailTokenView(TokenObtainPairView):
    serializer_class = EmailGetTokenSerializer