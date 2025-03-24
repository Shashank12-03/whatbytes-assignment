from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PatientSerializer

# Create your views here.
class AddPatientView(APIView):
    permisson_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post (self, request):
        
        try:
            name = request.data.get('name')
            address = request.data.get('address')
            age = request.data.get('age')
            weight = request.data.get('weight')
            height = request.data.get('height')
            gender = request.data.get('gender')
            patients_id = request.user.id
            patient = Patient.objects.create(patients_id=patients_id,name=name,address=address,age=age,weight=weight,height=height,gender=gender)
            patient.save()
            print(patient)
            return Response({'message':'Patient added successfully!!!'},status=status.HTTP_201_CREATED)

        except Exception as e:        
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListPatientView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self,request):
        try:
            
            patients = Patient.objects.filter(patients_id=request.user.id)
            serializer = PatientSerializer(patients,many=True)
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetPatientByIdView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self,request,pk):
        try:
            patient = Patient.objects.get(pk=pk,patients_id=request.user.id)
            if not patient:
                return Response({'message':'Patient not found !!!'},status=status.HTTP_400_BAD_REQUEST)
            
            serializer = PatientSerializer(patient)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
class UpdatePatientView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def put(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk, patients_id=request.user.id)
            if not patient:
                return Response({'message': 'Patient not found !!!'}, status=status.HTTP_400_BAD_REQUEST)

            name = request.data.get('name', patient.name)
            address = request.data.get('address', patient.address)
            age = request.data.get('age', patient.age)
            weight = request.data.get('weight', patient.weight)
            height = request.data.get('height', patient.height)
            gender = request.data.get('gender', patient.gender)

            patient.name = name
            patient.address = address
            patient.age = age
            patient.weight = weight
            patient.height = height
            patient.gender = gender
            patient.save()

            return Response({'message': 'Patient updated successfully!!!'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Oops something went wrong !!!', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeletePatientView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def delete(self,request,pk):
        try:
            patient = Patient.objects.get(pk=pk,patients_id=request.user.id)
            if not patient:
                return Response({'message':'Patient not found !!!'},status=status.HTTP_400_BAD_REQUEST)
            
            patient.delete()
            return Response({'message':'Patient deleted successfully!!!'},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message':'Oops something went wrong !!!','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)