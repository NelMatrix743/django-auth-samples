from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



# Create your views here.

def system_register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


def system_login(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")


def system_log_out(request: HttpRequest) -> HttpResponse:
    pass