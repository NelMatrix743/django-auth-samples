from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def system_home_view(request: HttpRequest) -> HttpResponse: 
    return render(request, "home/index.html")

# eosc