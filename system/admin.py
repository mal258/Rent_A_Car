from django.contrib import admin
from .models import Car, Order, PrivateMsg, Location, UserDetails
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ("car_name", "image", "company_name")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("date", "to", "Drivers_name")

class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")

class LocationAdmin(admin.ModelAdmin):
    list_display = ("loc_name", "address", "vehicle_cap")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","mobileno","birthdate","address","license_number","license_place",)

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(UserDetails, CustomerAdmin)