from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={
        'nome': 'Rachel Moreira'
    })

def pano(request, id):
    return render(request, 'panos-view.html', context={
        'nome': 'Rachel Moraes',
        })
