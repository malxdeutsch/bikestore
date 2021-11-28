from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Customer, Vehicle
from .forms import RentalForm, CustomerForm, VehicleForm
# Create your views here.

def rental (request):
    all_rentals = Rental.objects.all().order_by('return_date')
    return render (request, 'rental.html', {'all_rentals': all_rentals})

def rental_id (request, rentals_id):
    one_rental = Rental.objects.get (id = rentals_id)
    return render (request, 'one_rental.html', {'one_rental': one_rental})

def rental_add (request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            add_them = Rental.objects.create(**form.cleaned_data)
            return redirect('rental.html')
        else:
            raise ValidationError(_('Invalid value'))
   
    if request.method == 'GET':
        form = RentalForm()
        return render(request, 'add_rental.html', {'form': form})

def customer_id (request, customers_id):
    one_customer = Customer.objects.get (id= customers_id)
    return render (request, 'one_customer.html', {'one_customer': one_customer})

def customer (request):
    all_customers = Customer.objects.all().order_by('first_name')
    return render (request, 'customers.html', {'all_customers': all_customers})

def customer_add (request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        return redirect('customer')
    if request.method == 'GET':
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def vehicle (request):
    all_vehicles = Vehicle.objects.all().order_by('vehicle_type')
    return render (request, 'vehicle.html', {'all_vehicles': all_vehicles})

def vehicle_id (request, vehicles_id):
    one_vehicle = Vehicle.objects.get (id = vehicles_id)
    return render (request, 'one_vehicle.html', {'one_vehicle': one_vehicle})

def vehicle_add (request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        return redirect('vehicle')
    if request.method == 'GET':
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})
