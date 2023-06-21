from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def simple_view(request):
    return render(request,'first_app/example.html') #.html

def variable_view(request):

    my_var = {'first_name':'rosaLind', 'last_name':'franklin',
              'some_list':[1,2,3], 'user_logged_in':False}

    return render(request, 'first_app/variable.html',context=my_var) 