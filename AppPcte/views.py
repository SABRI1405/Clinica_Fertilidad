from django.shortcuts import render
from AppPcte.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render (request, "padre.html")

def registro(request):
    if request.method == "POST":
        paciente= Paciente(nombre=request.POST["nombre"], edad=request.POST["edad"], fecha_nacimiento=request.POST["fecha_nacimiento"])
        paciente.save()
        crio= Crio_Pte(estadio_C=request.POST["estadio_C"], cantidad_C=request.POST["cantidad_C"])
        crio.save()
        trasfer= Transfer_Pte(estadio_T=request.POST["estadio_T"], cantidad_T=request.POST["cantidad_T"])
        trasfer.save()
        return render (request, "formulario.html")
    return render (request, "formulario.html")

def busqueda_pcte(request):
    return render (request, "busqueda_pcte.html")

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        paciente= Paciente.objects.filter(nombre__icontains=nombre)
        return render (request, "resultado_pcte.html", {"paciente": paciente})
    else:
        return HttpResponse ("No se encuentra")
    #return HttpResponse (f"Estamos buscando el paciente : {request.GET ['nombre']}")




# Create your views here.
