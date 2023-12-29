from django.contrib import admin
from app.models import Vehicle
# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle_type', 'vehicle_model']