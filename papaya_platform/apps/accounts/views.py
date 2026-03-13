from django.http import HttpRequest, HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.http import require_POST



def system_register(request: HttpRequest) -> HttpResponse:
    """ user registration view """

    if request.method == "POST":
        error_messages = {}

        registration_data: QueryDict = request.POST

        first_name: str = registration_data.get("first_name")
        last_name: str = registration_data.get("last_name")
        user_name: str = registration_data.get("username")

        password: str = registration_data.get("password")
        confirm_password: str = registration_data.get("confirm_password")

        if User.objects.filter(username=user_name).exists():
            error_messages["user_err"] = "Username already exists"

        if password != confirm_password:
            error_messages["password_err"] = "Passwords do not match"

        if error_messages:
            context = {
                "errors" : error_messages,
                "data" : registration_data  # did not use this property in this project
            }
            return render(request, "accounts/register.html", context)
        
        user = User.objects.create_user(
            username=user_name,
            password=password
        )

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "accounts/register.html")


def system_login(request: HttpRequest) -> HttpResponse:
    """ user login view """

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
    """" user logout view """

    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


# eosc