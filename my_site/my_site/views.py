from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home_view(request):
    return HttpResponse("HOME")

def my_custom_page_not_found_view(request,exception):
    return render(request, '404.html',status=404)
    # 이 방법도 있지만 이런 방법 없이 404.html이라고
    # 작성하는 것이 더 강력하고 권장하는 방법이다.

