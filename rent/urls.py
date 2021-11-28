from django.urls import path
from .views import rental, rental_id, rental_add, customer_id, customer, vehicle, vehicle_id, customer_add, vehicle_add

urlpatterns = [
    path('rental/', rental, name = 'rental'),
    path('rental/<int:rentals_id>', rental_id, name = 'rentals_id'),
    path('rental/add/', rental_add, name = 'add_rental'),
    path('customer/<int:customers_id>/', customer_id, name = 'customers_id'),
    path('customer/', customer, name = 'customer'),
    path('customer/add/', customer_add, name = 'add_customer'),
    path('vehicle/', vehicle, name = 'vehicle'),
    path('vehicle/<int:vehicles_id>', vehicle_id, name = 'vehicles_id'),
    path('vehicle/add/', vehicle_add, name = 'add_vehicle'),


]