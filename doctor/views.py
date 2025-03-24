from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DoctorSerializer

# Create your views here.
class AddDoctorView(APIView):
    permisson_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post (self, request):
        
        try:
            name = request.data.get('name')
            address = request.data.get('address')
            specialization = request.data.get('specialization')
            phone_number = request.data.get('phone_number')
            doctors_id = request.user.id
            doctor = Doctor.objects.create(doctors_id=doctors_id,name=name,address=address, specialization=specialization, phone_number=phone_number)
            doctor.save()
            print(doctor)
            return Response({'message':'Patient added successfully!!!'},status=status.HTTP_201_CREATED)

        except Exception as e:        
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListDoctorView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self,request):
        try:
            
            doctor = Doctor.objects.filter(doctors_id=request.user.id)
            serializer = DoctorSerializer(doctor,many=True)
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetDoctorByIdView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self,request,pk):
        try:
            doctor = Doctor.objects.get(pk=pk,doctors_id=request.user.id)
            if not doctor:
                return Response({'message':'Doctor not found !!!'},status=status.HTTP_400_BAD_REQUEST)
            
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
class UpdateDoctorView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk, doctors_id=request.user.id)
            if not doctor:
                return Response({'message': 'Doctor not found !!!'}, status=status.HTTP_400_BAD_REQUEST)
            
            name = request.data.get('name', doctor.name)
            address = request.data.get('address', doctor.address)
            specialization = request.data.get('specialization', doctor.specialization)
            phone_number = request.data.get('phone_number', doctor.phone_number)
            
            doctor.name = name
            doctor.address = address
            doctor.specialization = specialization
            doctor.phone_number = phone_number
            doctor.save()
            
            return Response({'message': 'Doctor updated successfully!!!'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Oops something went wrong !!!', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteDoctorView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def delete(self,request,pk):
        try:
            doctor = Doctor.objects.get(pk=pk,doctors_id=request.user.id)
            if not doctor:
                return Response({'message':'Doctor not found !!!'},status=status.HTTP_400_BAD_REQUEST)
            
            doctor.delete()
            return Response({'message':'Doctor deleted successfully!!!'},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)