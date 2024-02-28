from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse 
from django.shortcuts import render

from .forms import *


def index(request):
    return render(request, "core/index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html") 


class CustomLoginView(LoginView):
    authentication_form =  CustomAuthenticationForm
    template_name = "core/login.html"
     
    
