from django.shortcuts import get_object_or_404, render
from .models import Matricula

# Create your views here.

def index(requests):
    alunos = Matricula.objects.all()
    return render(requests,"index.html",{'alunos_nome':alunos})

def matriculas(requests, id):
    alunos = Matricula.objects.get(id=id)
    return render(requests,"matriculas.html",{'alunos':alunos})
