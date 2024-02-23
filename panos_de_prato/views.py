from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', context={
        'nome': 'Rachel Moreira'
    })

def contato(request):
    return HttpResponse('Contatos')
