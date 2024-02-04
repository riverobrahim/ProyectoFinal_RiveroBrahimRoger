from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100) #esta clase posee un modelo para texto charfield con parametro obligatorio de largo max de caracteres

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "país" 
        verbose_name_plural = "paises"
        
        

class Cliente(models.Model):
    nombre = models.CharField(max_length=100) #se repite las caracteristicas de clase pais
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True) #en este caso como es dato numerico par a la clase fecha se usa DateField con parametros null=True para poder dejar en blanco en la base de datos , tambien  blank=True para informarle a python de que es posible dejar en blanco 
    pais_origen_id = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"