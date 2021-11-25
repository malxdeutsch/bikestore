from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Customer (models.Model):
    first_name = models.CharField (max_length =200 )
    last_name = models.CharField (max_length =200 )
    email = models.EmailField (max_length =200 )
    phone_number = models.CharField (max_length =200 )
    address = models.CharField (max_length =200 )
    city = models.CharField (max_length =200 )
    country = models.CharField (max_length =200 )

class Vehicle (models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete = models.CASCADE)
    date_created = models.DateField()
    real_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    size = models.ForeignKey( 'VehicleSize', on_delete = models.CASCADE)

class VehicleType (models.Model):
    name = models.CharField (max_length =200 )

class VehicleSize (models.Model):
    name = models.CharField (max_length =200 )

class Rental (models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey( Customer, on_delete = models.CASCADE)
    vehicle = models.ForeignKey( Vehicle, on_delete = models.CASCADE)

class RentalRate (models.Model):
    daily_rate = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    vehicle_type =models.ForeignKey( VehicleType, on_delete = models.CASCADE)
    vehicle_size =models.ForeignKey( VehicleSize, on_delete = models.CASCADE)

