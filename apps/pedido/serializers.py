from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Componente,Rol,TipoComponente,Usuario,Orden,DetalleOrden

class TipoComponenteSerializer(serializers.ModelSerializer):
    class Meta:
       model = TipoComponente
       fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'






    

    