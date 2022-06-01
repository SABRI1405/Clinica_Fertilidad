from django.urls import path
#IMPORTAR LAS VIEWS
from . import views

urlpatterns = [
    path("", views.inicio),
    path("registro", views.registro),
    path("busqueda_pcte", views.busqueda_pcte),
    path("buscar", views.buscar),

]