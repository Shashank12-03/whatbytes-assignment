from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .models import Mapping
from patients.models import Patient
from doctor.models import Doctor

class CreateMappingView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            patient_id = request.data.get('patient_id')
            doctor_id = request.data.get('doctor_id')

            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
            if not patient or not doctor:
                return Response({'message': 'Patient or Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
            
            mapping = Mapping.objects.create(patient=patient, doctor=doctor)
            
            return Response({'message': 'Mapping created successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Error creating mapping', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListMappingsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            mappings = Mapping.objects.all()
            data = [
                {
                    'id': mapping.id,
                    'patient': mapping.patient.name,
                    'doctor': mapping.doctor.name
                }
                for mapping in mappings
            ]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error retrieving mappings', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetMappingsByPatientView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, patient_id):
        try:
            mappings = Mapping.objects.filter(patient_id=patient_id)
            data = [
                {
                    'id': mapping.id,
                    'doctor': mapping.doctor.name
                }
                for mapping in mappings
            ]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error retrieving mappings', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteMappingView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, id):
        try:
            mapping = Mapping.objects.get(id=id)
            mapping.delete()
            return Response({'message': 'Mapping deleted successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error deleting mapping', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)