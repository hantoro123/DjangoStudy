from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home_view(request):
    return HttpResponse("HOME")

def my_custom_page_not_found_view(request,exception):
    return render(request, 'error_view.html',status=404)

