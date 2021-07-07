from django.shortcuts import redirect, render
from .models import Colaboradores
from .forms import ColaboradoresForm

# Create your views here.

def home(request):
    
    colaborador= Colaboradores.objects.all()
    
    return render(request, 'home.html', context={'usuarios':colaborador})

def form_Colaboradores(request):
    if request.method=='POST':
        colaboradores_form = ColaboradoresForm(request.POST)
        if colaboradores_form.is_valid():
              colaboradores_form.save()
              return redirect('form_Colaboradores')
    else:
        colaboradores_form=ColaboradoresForm()


    return render(request, 'core/form_Colaboradores.html',{'colaboradores_form':colaboradores_form})

def ver_Colaboradores(request):
    colaborador=Colaboradores.objects.all()

    
    return render (request, 'core/ver_Colaboradores.html',{'colaborador':colaborador})

def form_mod_Colaboradores(request, id):

    colaborador = Colaboradores.objects.get(idColaboradores=id)
    datos={
        'form': ColaboradoresForm(instance=colaborador)
    }

    if request.method =='POST':
        formulario =ColaboradoresForm(data=request.POST , instance=colaborador)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')

    return render(request, 'core/form_mod_Colaboradores.html', datos)