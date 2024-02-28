from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
CreateView,
UpdateView,
DeleteView,
DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import *
from .forms import * 
  

def index(request):
    return render(request, "producto/index.html")

#def productocategoria_list(request):
   # categorias = ProductoCategoria.objects.all()
   # context = {"object_list": categorias}
   # return render(request, "producto/productocategoria_list.html", context) 

class ProductoCategoriaList(ListView):
    model = ProductoCategoria 
    
    def get_query(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = ProductoCategoria.objects.all()
        return object_list    
            
#def productocategoria_form(request):
#    if request.method =="POST":
#        form = ProductoCategoriaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("producto:productocategoria_list")
        
#    else: #request.method == "GET":
#        form = ProductoCategoriaForm()
#    return render(request, "producto/productocategoria_form.html", {"form" : form})
        
              
        
  
        
class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")         
    
#def productocategoria_update(request, pk: int):
#    consulta = ProductoCategoria.objects.get(id=pk)
#    if request.method =="POST":
#        form = ProductoCategoriaForm(request.POST, instance=consulta)
#        if form.is_valid():
#            form.save()
#            return redirect("producto:productocategoria_list")
#    else: #request.method == "GET":
#        form = ProductoCategoriaForm(instance=consulta)
#    return render(request, "producto/productocategoria_form.html", {"form" : form})


class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
    
#def productocategoria_delete(request, pk : int):
#    consulta =  ProductoCategoria.objects.get(id=pk)
#    if request.method == "POST":
#        consulta.delete()
#        return redirect("producto:productocategoria_list")
#    return render(request, "producto/productocategoria_confirm_delete.html", {"object" : consulta }) 

class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")  
    
    
#def productocategoria_detail(request, pk):
#    consulta = ProductoCategoria.objects.get(id=pk)
#    return render(request, "producto/productocategoria_detail.html", {"object" : consulta})
    
    
class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria