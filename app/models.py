from django.db import models

# Create your models here.

class Vehicle(models.Model):

    types = (('--select type--', '--select type--'),('two', 'Two wheelers'),('three','three wheelers'),('four','four wheelers'))

    vehicle_no = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50, choices=types, default='--select type--')
    vehicle_model = models.TextField()
    vehicle_desc = models.TextField()