from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
    def create(self, validated_data):
        if validated_data:
            print(validated_data)
            patent =  Patient.objects.create(**validated_data)
            return patent
        return None
    