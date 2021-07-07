from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Colaboradores

class ColaboradoresForm(ModelForm):



    class Meta:
        model=Colaboradores
        fields=['idColaboradores','nomColaboradores','telefono','direccion','email','pais']

        labels={
            'idColaboradores': 'RUT: ',
            'nomColaboradores': 'Nombre: ',
            'telefono': 'Telefono: ',
            'direccion':'Direccion: ',
            'email': 'Email: ',
            'pais':'Pais: ',
            }

        widgets={

            'idColaboradores': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su RUT',
                    'id':'idColaboradores'
                }
            ),

            'nomColaboradores': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id':'nomColaboradores'
                }
            ),

            'telefono': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Telefono',
                    'id':'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Direccion',
                    'id':'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su email',
                    'id':'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Pais',
                    'id':'pais'
                }
            ),
        }