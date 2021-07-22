from django.http import request
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
              return redirect('home')
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

def form_del_Colaboradores(request, id):

    colaborador=Colaboradores.objects.get(idColaboradores=id)
    colaborador.delete()
    return redirect(to="ver_Colaboradores")


from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ColaboradoresSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])


def lista_Colaboradores(request): 

    if request.method == 'GET': 
        colaborador = Colaboradores.objects.all()
        serializer =ColaboradoresSerializer(colaborador, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        data = JSONParser().parse(request)
        serializer = ColaboradoresSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def lista_api(request):
    return render(request, 'API.html')

@api_view(['GET','PUT', 'DELETE'])

def detalle_Colaboradores(request,id):
    try:
        colaborador=Colaboradores.objects.get(idColaboradores=id)
    except Colaboradores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= ColaboradoresSerializer(colaborador)
        return Response (serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ColaboradoresSerializer(colaborador, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        colaborador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

