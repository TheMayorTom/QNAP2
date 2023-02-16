from django.shortcuts import render, redirect
from .models import Inventario

# Create your views here.

def home(request):
    inventarios = Inventario.objects.all()
    return render(request, 'gestionInventario.html', {'inventarios' : inventarios})

def registrarPrograma(request):
    Grado = request.POST['txtGrado']
    Materia = request.POST['txtMateria']
    Nombre = request.POST['txtNombre']
    Nom_archivo_ubi = request.POST['txtNom_archivo_ubi']
    Serie = request.POST['txtSerie']
    Peso = request.POST['txtPeso']
    Ubicacion = request.POST['txtUbicacion']
    Ruta = request.POST['txtRuta']

    inventario = Inventario.objects.create(Grado=Grado, Materia=Materia, Nombre=Nombre, Nom_archivo_ubi=Nom_archivo_ubi, Serie=Serie, Peso=Peso, Ubicacion=Ubicacion, Ruta=Ruta)
    return redirect('/')

def eliminarPrograma(request, Nombre):
    inventario = Inventario.objects.get(Nombre=Nombre)
    inventario.delete()

    return redirect('/')

def editarPrograma(request, Nombre):
    inventario = Inventario.objects.get(Nombre=Nombre)
    return render(request, "editarPrograma",{"inventario": inventario})

def edicionPrograma(request):
    Grado = request.POST['txtGrado']
    Materia = request.POST['txtMateria']
    Nombre = request.POST['txtNombre']
    Nom_archivo_ubi = request.POST['txtNom_archivo_ubi']
    Serie = request.POST['txtSerie']
    Peso = request.POST['txtPeso']
    Ubicacion = request.POST['txtUbicacion']
    Ruta = request.POST['txtRuta']

    inventario = Inventario.objects.get(Nombre=Nombre)
    inventario.Grado = Grado
    inventario.Materia = Materia
    inventario.Nombre = Nombre
    inventario.Nom_archivo_ubi = Nom_archivo_ubi
    inventario.Serie = Serie
    inventario.Peso = Peso
    inventario.Ubicacion = Ubicacion
    inventario.Ruta = Ruta
    inventario.save()
    return redirect('/')

