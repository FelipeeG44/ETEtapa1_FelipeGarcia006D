from django.shortcuts import render
from .models import Colaboradores

# Create your views here.

def home(request):
    
    colaborador= Colaboradores.objects.all()
    
    return render(request, 'core/home.html', context={'usuarios':colaborador})

def form_Colaboradores(request):
    return render(request, 'core/form_Colaboradores.html')