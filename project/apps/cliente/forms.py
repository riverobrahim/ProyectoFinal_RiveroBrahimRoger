from django import forms

from . import models 

class Clienteform(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"