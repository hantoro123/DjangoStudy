from django.urls import path
from . import views

# register the app namespace
# URL Names
app_name = 'first_app'

urlpatterns = [
    path('', views.simple_view, name='example'), # domain.com /first_app
    path('variable/', views.variable_view, name='variable'),
]