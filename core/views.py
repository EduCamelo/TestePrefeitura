from django.shortcuts import render, redirect
from .models import Endereco


def home(request):
    links = Endereco.objects.all()
    return render(request, 'index.html', {'links': links})


def salvar(request):
    var_nome = request.POST.get('nome')
    var_link = request.POST.get('link')
    Endereco.objects.create(link=var_link, nome=var_nome)
    return redirect(home)


def editar(request, id):
    link = Endereco.objects.get(id=id)
    return render(request, "update.html", {'link': link})


def update(request, id):
    var_nome = request.POST.get('nome')
    var_link = request.POST.get('link')
    link = Endereco.objects.get(id=id)
    link.link = var_link
    link.nome = var_nome
    link.save()
    return redirect(home)


def delete(request, id):
    link = Endereco.objects.get(id=id)
    link.delete()
    return redirect(home)
    

def testelegal(request):
    links = Endereco.objects.all()
    return render(request, 'testelegal.html', {'links': links})
