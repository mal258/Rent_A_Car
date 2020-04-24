from django import forms
from .models import Car, Order, PrivateMsg, Location, UserDetails, StartSubscribe

LOCATION_CHOICES= [('view'),('add'),]

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

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
            "loc_zip",
            "loc_name",
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
        fields = ["first_name",
                  "start_date",
                  "payment_type",
                  "credit_card_number",
                  "credit_card_name",
                  "expiry_date",
                  "cvv",
        ]

# class CreateBookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ('vehicle_type', 'start_time', 'end_time')
#         exclude = ('user',)
#
#     depot_list = Location.objects.depots()
#     vehicle_list = Car.objects.vehicles()
#
#     depot = forms.ChoiceField(choices=[(depot.depot, depot.depot) for depot in depot_list])
#     vehicle_type = forms.ChoiceField(
#         choices=[(vehicle_type.car_type, vehicle_type.car_type) for vehicle_type in vehicle_list])
#     start_time = forms.DateTimeField()
#     end_time = forms.DateTimeField()

