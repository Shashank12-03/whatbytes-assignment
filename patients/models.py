from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='patients')
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=())
    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name