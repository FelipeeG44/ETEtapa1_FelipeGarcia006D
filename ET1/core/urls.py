from django import urls
from django.urls import path
from .views import home, form_Colaboradores, form_mod_Colaboradores,ver_Colaboradores,form_del_Colaboradores,lista_Colaboradores, detalle_Colaboradores, lista_api 

urlpatterns = [
    path('', home, name="home"),
    path('lista_api', lista_api, name="lista_api"),
    path('form_Colaboradores', form_Colaboradores, name="form_Colaboradores"),
    path('form_mod_Colaboradores/<id>', form_mod_Colaboradores, name="form_mod_Colaboradores"),
    path('ver_Colaboradores', ver_Colaboradores, name="ver_Colaboradores"),
    path('form_del_Colaboradores/<id>', form_del_Colaboradores, name="form_del_Colaboradores"),
    path('lista_Colaboradores', lista_Colaboradores ,name="lista_Colaboradores"),
    path('detalle_Colaboradores/<id>', detalle_Colaboradores, name="detalle_Colaboradores")
    
    
]