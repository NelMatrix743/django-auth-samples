from django.urls import path
from .views import system_home_view



app_name: str = "home"

urlpatterns: list = [
    path('', system_home_view, name="home"),
]