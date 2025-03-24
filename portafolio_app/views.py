from django.shortcuts import render
from .models import Project, Skill

def home(request):
    return render(request, 'home.html')

def habilidades(request):
    return render(request, 'habilidades.html')

def proyectos(request):
    return render(request, 'proyectos.html')
