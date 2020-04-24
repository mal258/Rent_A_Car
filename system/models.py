from django.db import models
#import django_tables2 as tables

#from multiselectfield import MultiSelectField
from django import forms
def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.car_name,filename)

CAR_TYPE = (
        ('small car', 'SMALL CAR'),
        ('full-size_car', 'FULL-SIZE CAR'),
        ('truck', 'TRUCK'),
        ('luxury', 'LUXURY')
        )


class Order(models.Model):
    Drivers_name = models.CharField(max_length=100,unique=True)
    license_number = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return self.Drivers_name

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)

class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

#shreyus
class Location(models.Model):
    loc_zip = models.IntegerField()
    loc_name = models.CharField(max_length=200)
    loc_id = models.IntegerField()
    address = models.TextField()
    vehicle_cap = models.IntegerField(default=0)

    def __str__(self):
        return self.loc_name

class Car(models.Model):

    image = models.ImageField(upload_to=uploaded_location,null=True, blank=True)
    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=50, choices=CAR_TYPE)
    model = models.IntegerField()
    num_of_seats = models.IntegerField()
    reg_tag = models.CharField(max_length=100)
    cur_milage = models.IntegerField()
    last_serv = models.IntegerField()
    cost_per_day = models.CharField(max_length=50)
    depot = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='vehicle')
    zipcode = models.CharField(max_length=50)
    like = models.IntegerField(default=0)
    class vehicle(models.TextChoices):
        Good = 'Good'
        Need_cleaning = 'Need Cleaning'
        Need_maintenance = 'Needs Maintenance'
    vehicle_cond = models.CharField(max_length=100, choices=vehicle.choices)
    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class UserDetails(models.Model):
    first_name = models.CharField(max_length=30,unique=True)
    last_name = models.CharField(max_length=30)
    mobileno = models.IntegerField()
    birthdate = models.DateField()
    address = models.CharField(max_length=30)
    license_number = models.CharField(max_length=10)
    license_place = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class StartSubscribe(models.Model):

    first_name = models.CharField(max_length=30,unique=True)
    start_date = models.DateField()
    payment_type = models.CharField(max_length=10)
    credit_card_number = models.IntegerField()
    credit_card_name = models.CharField(max_length=30)
    expiry_date = models.DateField()
    cvv = models.IntegerField()


    def __str__(self):
        return self.credit_card_number

class Booking(models.Model):
    customer = models.ForeignKey(UserDetails, on_delete=models.CASCADE,related_name='customer')
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='vehicle')
    depot = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='depot')

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}".format(self.customer.first_name,self.vehicle.car_name, self.depot.loc_name,
                                           self.start_time, self.end_time)







 #   def get_absolute_url(self):
  #      return "/car/detail/%s/" % (self.id)