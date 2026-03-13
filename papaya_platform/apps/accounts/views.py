from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.conf import settings

from django.views.decorators.http import require_POST


# Create your views here.

def system_register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


def system_login(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")


@require_POST
def system_log_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


# eosc