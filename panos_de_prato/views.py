from django.shortcuts import render
from utils.fabrica import make_recipe
from .models import Panos, Categoria

def home(request):
    panos = Panos.objects.filter(esta_publicado=True).order_by('-id')
    return render(request, 'home.html', context={
        'panos': panos,
    })

def pano(request, id):
    return render(request, 'panos-view.html', context={
        'pano': make_recipe(),
        'is_detail_page': True,
        })

def categoria(request, categoria_id):
    panos = Panos.objects.filter(categoria__id=categoria_id, esta_publicado=True).order_by('-id')
    return render(request, 'categoria.html', context={
        'panos': panos,
    })
