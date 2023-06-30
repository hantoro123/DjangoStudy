from django.urls import path
from . import views

# domain.com/office --> list of all the patient
urlpatterns = [
    path('', views.list_patients, name='list_patients'),
]