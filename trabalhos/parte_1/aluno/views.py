from django.shortcuts import redirect, render
from .models import Matricula
from .forms import ContatoForm

# Create your views here.

def index(requests):
    alunos = Matricula.objects.all()
    return render(requests,"index.html",{'alunos_nome':alunos})

def matriculas(requests, id):
    alunos = Matricula.objects.get(id=id)
    return render(requests,"matriculas.html",{'alunos':alunos})

def contato(requests):
    form = ContatoForm(requests.POST or None)
    context = {'form':form}
    if requests.method == 'POST':

        if form.is_valid():
            form.send_mail()
        else:
            print("Email nao enviado")
        return redirect('index')
    return render(requests,"FaleConosco.html", context)