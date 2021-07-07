from django import urls
from django.urls import path
from .views import home, form_Colaboradores

urlpatterns = [
    path('', home, name="home"),
    path('form-Colaboradores', form_Colaboradores, name="form_Colaboradores"),
]