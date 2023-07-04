from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('rental_view/', views.rental_review, name='rental_view'),
    path('thank_you/', views.thank_you, name='thank_you'),
]