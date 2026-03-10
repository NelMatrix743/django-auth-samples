from django.urls import path
from .views import system_register, system_login, system_log_out



app_name: str = "accounts"

urlpatterns: list = [
    path("register/", system_register, name="register"),
    path("login/", system_login, name="login"),
    path("logout/", system_log_out, name="logout"),
]