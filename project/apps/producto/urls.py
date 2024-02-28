from django.urls import path

from .views import *

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    #path("producto/list", views.productocategoria_list, name="productocategoria_list"),
    path("producto/list", ProductoCategoriaList.as_view(), name="productocategoria_list"),
    #path("producto/form", views.productocategoria_form, name="productocategoria_form"),
    path("producto/form/", ProductoCategoriaCreate.as_view(), name="productocategoria_form"),
    #path("producto/update/<int:pk>/", views.productocategoria_update, name="productocategoria_update"),
    path("producto/update/<int:pk>/", ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    #path("producto/delete/<int:pk>/", views.productocategoria_delete, name="productocategoria_delete"),
    path("producto/delete/<int:pk>/", ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
    path("producto/detail/<int:pk>/", ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
]



    