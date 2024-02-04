from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pais/list/", views.pais_list, name="pais_list"),
    path("cliente/list/", views.cliente_list, name="cliente_list"),
    
]
