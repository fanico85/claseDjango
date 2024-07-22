from AppCoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def curso(request, nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    return HttpResponse(documento)

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse('vista de profesores')

def estudiantes(request):
    return HttpResponse('vista de estudiantes')

def entregables(request):
    return HttpResponse('vista de entregables')