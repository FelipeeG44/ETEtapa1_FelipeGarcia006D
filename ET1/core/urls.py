from django import urls
from django.urls import path
from .views import home, form_Colaboradores, form_mod_Colaboradores ,ver_Colaboradores,form_del_Colaboradores

urlpatterns = [
    path('', home, name="home"),
    path('form-Colaboradores', form_Colaboradores, name="form_Colaboradores"),
    path('form-mod-Colaboradores/<id>', form_mod_Colaboradores, name="form_mod_Colaboradores"),
    path('ver-Colaboradores', ver_Colaboradores, name="ver_Colaboradores"),
    path('form-del-Colaboradores/<id>', form_del_Colaboradores, name="form_del_Colaboradores")
]