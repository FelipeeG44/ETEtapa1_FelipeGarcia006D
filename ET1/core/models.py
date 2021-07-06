from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    idColaboradores= models.CharField(max_length=10 ,primary_key=True ,verbose_name="RUT Colaborador")
    nomColaboradores= models.CharField(max_length=30, verbose_name="Nombre Colaborador")
    telefono=models.IntegerField(verbose_name="Telefono")
    direccion=models.CharField(max_length=30,verbose_name="Dirección")
    email=models.CharField(max_length=30,verbose_name="Email")
    pais=models.CharField( max_length=20,verbose_name="país")

    def __str__(self):
        return self.idColaboradores
