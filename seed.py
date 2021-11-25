from faker import Faker
import os
import django
import random

fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import *

def create_vehicle():
    for _ in range (5):
        Vehicle.objects.create(vehicle_type = random.choice(VehicleType.objects.all()),
        date_created = fake.date(),
        real_cost = 5,
        size = random.choice(VehicleSize.objects.all()))

# create_vehicle()


def create_rental(num =100):
    for _ in range(num):
        first = fake.date()
        second = fake.date()
        if first < second:
            Rental.objects.create (rental_date = first, return_date = second, customer = random.choice(Customer.objects.all()), 
            vehicle = random.choice(Vehicle.objects.all()))
        else:
            Rental.objects.create (rental_date = second, return_date = first, customer = random.choice(Customer.objects.all()), 
            vehicle = random.choice(Vehicle.objects.all()))

# Rental.objects.all().delete()
# create_rental()