from django import forms
from .models import Car, Order, PrivateMsg, Location

LOCATION_CHOICES= [
    ('view'),
    ('add'),
    ]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "image",
            "car_name",
            "company_name",
            "num_of_seats",
            "cost_par_day",
            "content",
        ]
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "Drivers_name",
            "license_number",
            "cell_no",
            "address",
            "date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]
#shreyus
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            "loc_name",
            "address",
            "vehicle_cap",
        ]
