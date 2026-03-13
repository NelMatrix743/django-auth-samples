from django.http import HttpRequest, HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.conf import settings

from django.views.decorators.http import require_POST


# Create your views here.

def system_register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


def system_login(request: HttpRequest) -> HttpResponse:
    error_messages = {}

    if request.method == "POST":
        login_creds: QueryDict = request.POST
        user_name: str = login_creds.get("username")
        user_password: str = login_creds.get("password")

        user = authenticate(
            request,
            username=user_name,
            password=user_password
        )

        if user:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        
        error_messages["login_error"] = "Invalid username or password"

    context = {
        "errors" : error_messages
    }

    return render(request, "accounts/login.html", context)


@require_POST
def system_log_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


# eosc