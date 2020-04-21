from django import forms
from .models import Car, Order, PrivateMsg, Location, UserDetails, StartSubscribe

LOCATION_CHOICES= [('view'),('add'),]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "image",
            "car_name",
            "car_type",
            "model",
            "reg_tag",
            "num_of_seats",
            "cur_milage",
            "last_serv",
            "cost_per_day",
            "vehicle_cond",
            "rent_loc",
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
            "loc_zip",
            "loc_id",
            "address",
            "vehicle_cap",
        ]

class UserDetail(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            "first_name",
            "last_name",
            "mobileno",
            "birthdate",
            "address",
            "license_number",
            "license_place",
        ]
class StartSubcription(forms.ModelForm):
    # start_date =forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    # widget = {
    #     'start_date':forms.TextInput(attrs={'class':'datepicker'})}
    class Meta:
        model = StartSubscribe
        fields = ["start_date",
            "payment_type",
                  "credit_card_number",
                  "credit_card_name",
                  "expiry_date",
                  "cvv",
        ]