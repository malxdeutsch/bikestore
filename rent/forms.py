from django import forms
from .models import Rental, Customer, Vehicle, VehicleType, VehicleSize

class RentalForm(forms.Form):
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle_id = forms.ModelChoiceField(queryset=Vehicle.objects.all())

class CustomerForm(forms.Form):
    first_name = forms.CharField (max_length =200 )
    last_name = forms.CharField (max_length =200 )
    email = forms.EmailField (max_length =200 )
    phone_number = forms.CharField (max_length =200 )
    address = forms.CharField (max_length =200 )
    city = forms.CharField (max_length =200 )
    country = forms.CharField (max_length =200 )

class VehicleForm(forms.Form):
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    real_cost = forms.CharField()
    size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())
    