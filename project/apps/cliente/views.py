from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models
from . import forms  



def index(request):
    return render(request,"cliente/index.html")

def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "cliente/pais_list.html", context)

def cliente_list(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes":clientes}
    return render(request, "cliente/cliente_list.html", context)

def cliente_create(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.Clienteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:cliente_list")
    else: #if request.method == "GET":
        form = forms.Clienteform()
    return render(request, "cliente/cliente_create.html", {"form" : form})