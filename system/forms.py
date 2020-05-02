from django import forms
from .models import Car, Order, PrivateMsg, Location, UserDetails, StartSubscribe, Booking
from django.contrib.auth import get_user_model
from .manager import *
from .choices import DEPOTS, CAR_TYPE

User = get_user_model()

LOCATION_CHOICES = [('view'), ('add'), ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
 #       exclude = ('late_fee',)


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


# shreyus
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            "loc_zip",
            "loc_name",
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
            "payment_type",
            "credit_card_number",
            "credit_card_name",
            "expiry_date",
            "cvv",
        ]


class StartSubcription(forms.ModelForm):
    # start_date =forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    # widget = {
    #     'start_date':forms.TextInput(attrs={'class':'datepicker'})}
    class Meta:
        model = StartSubscribe
        fields = ["first_name",
                  "start_date",
                  "payment_type",
                  "credit_card_number",
                  "credit_card_name",
                  "expiry_date",
                  "cvv", ]


class DeleteUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",

        ]


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('vehicle_type', 'start_time', 'end_time')
        exclude = ('user',)

    depot_list = Location.objects.depots()
    vehicle_list = Car.objects.cars()
    print(vehicle_list)

    # depot = forms.ChoiceField(choices=[(depot.loc_name, depot.loc_name) for depot in depot_list])
    # vehicle_type = forms.ChoiceField(choices=[(vehicle_type.car_type, vehicle_type.car_type) for vehicle_type in vehicle_list])
    depot = forms.ChoiceField(choices=DEPOTS)
    vehicle_type = forms.ChoiceField(choices=CAR_TYPE)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
