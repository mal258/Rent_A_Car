from django.contrib import admin
from .models import Car, Order, PrivateMsg, Location
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "image", "company_name")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("date", "to", "Drivers_name")

class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")

class LocationAdmin(admin.ModelAdmin):
    list_display = ("loc_name", "address", "vehicle_cap")

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
admin.site.register(Location, LocationAdmin)