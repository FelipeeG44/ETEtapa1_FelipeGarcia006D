from django.db.models import fields
from rest_framework import serializers
from .models import Colaboradores

class ColaboradoresSerializer(serializers.ModelSerializer):
      class Meta:
          model = Colaboradores
          fields = ['idColaboradores', 'nomColaboradores', 'telefono', 'direccion', 'email', 'pais']
