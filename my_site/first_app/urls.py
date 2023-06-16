from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view), # domain.com /first_app
    path('variable/', views.variable_view),
]