from rest_framework import viewsets
from .serializers import TipoComponenteSerializer,ComponenteSerializer,OrdenSerializer,DetalleOrdenSerializer
from .models import Componente,Rol,TipoComponente,Usuario,Orden,DetalleOrden

class TipoComponenteViewSet(viewsets.ModelViewSet):
    serializer_class=TipoComponenteSerializer
    queryset = TipoComponente.objects.all()

class ComponenteViewSet(viewsets.ModelViewSet):
    serializer_class=ComponenteSerializer
    # queryset = Componente.objects.all()

    def get_queryset(self):
        queryset = Componente.objects.all()
        id_tipo = self.request.query_params.get('id_tipo', None)
        if id_tipo is not None:
            queryset = queryset.filter(id_tipo_id=id_tipo)
        return queryset


class OrdenViewSet(viewsets.ModelViewSet):
    serializer_class=OrdenSerializer
    queryset = Orden.objects.all()

class DetalleOrdenViewSet(viewsets.ModelViewSet):
    serializer_class=DetalleOrdenSerializer
    queryset = DetalleOrden.objects.all()