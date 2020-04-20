from django.db import models

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
# CHARGE = [
#      ('1-5hours'),
#      ('6-10hours')
#      ]
# CONDITION = (
#     ('Good'),
#     ('Needs Cleaning'),
#     ('Needs Maintenance')
# )

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
    rent_loc = models.IntegerField()
    like = models.IntegerField(default=0)
    class vehicle(models.TextChoices):
        Good = 'Good'
        Need_cleaning = 'Need Cleaning'
        Need_maintenance = 'Needs Maintenance'
    vehicle_cond = models.CharField(max_length=100, choices=vehicle.choices)
    # class cost(models.TextChoices):
    #     first = '1-5hours'
    #     second = '6-10hours'
    # cost = models.CharField(max_length=50, choices=cost.choices)


    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class Order(models.Model):
    Drivers_name = models.CharField(max_length=100)
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
    loc_name = models.CharField(max_length=200)
    loc_zip = models.IntegerField()
    loc_id = models.IntegerField()
    address = models.TextField()
    vehicle_cap = models.IntegerField(default=0)

    def __str__(self):
        return self.loc_name

class UserDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobileno = models.IntegerField()
    birthdate = models.DateField()
    address = models.CharField(max_length=30)
    license_number = models.CharField(max_length=10)
    license_place = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class start_subscription(models.Model):

    start_date = models.DateField()
    payment_type = models.CharField(max_length=10)
    credit_card_number = models.IntegerField()
    credit_card_name = models.CharField(max_length=30)
    expiry_date = models.DateField()
    cvv = models.IntegerField()


    def __str__(self):
        return self.credit_card_number






 #   def get_absolute_url(self):
  #      return "/car/detail/%s/" % (self.id)