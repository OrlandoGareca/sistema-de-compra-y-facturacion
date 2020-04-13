from django.urls import path,include
from app.api.views import ProductoList,ProductoDetalle
from rest_framework import routers, serializers, viewsets
urlpatterns = [
    path('v1/productos/',ProductoList.as_view(),name="producto_list"),
    path('v1/productos/<str:codigo>',ProductoDetalle.as_view(),name="producto_detalle"),

]
