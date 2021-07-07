from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Colaboradores

class ColaboradoresForm(ModelForm):



    class Meta:
        model=Colaboradores
        fields=['RUT','nombre','telefono','direccion','email','pais']