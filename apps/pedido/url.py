from django.urls import path
from .viewsets import TipoComponenteViewSet,ComponenteViewSet,OrdenViewSet,DetalleOrdenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tipoComponente',TipoComponenteViewSet)
router.register(r'Componente',ComponenteViewSet,base_name='Componente')
router.register(r'Orden',OrdenViewSet)
router.register(r'DetalleOrden',DetalleOrdenViewSet)

urlpatterns =router.urls
