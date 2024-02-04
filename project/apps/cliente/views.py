from django.shortcuts import render

from . import models


def index(request):
    context = {"app_name": "VirtualPlanet"}
    return render(request,"cliente/index.html", context)

def pais_list(request):
    paises = models.Pais.objects.all()
    return render(request, "cliente/pais_list.htmal ", {"paises":paises })

def cliente_list(request):
    clientes = models.Pais.objects.all()
    return render(request, "cliente/cliente_list.htmal ", {"clientes":clientes })