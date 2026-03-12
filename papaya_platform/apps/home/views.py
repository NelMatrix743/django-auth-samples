from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



# Create your views here.

def system_home_view(request: HttpRequest) -> HttpResponse: 
    return render(request, "home/index.html")
