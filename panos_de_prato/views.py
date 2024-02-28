from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.fabrica import make_recipe
from .models import Panos, Categoria

def home(request):
    panos = Panos.objects.filter(esta_publicado=False).order_by('-id')
    return render(request, 'home.html', context={
        'panos': panos,
    })

def pano(request, id):
    pano = get_object_or_404(Panos, pk=id, esta_publicado=True)
    return render(request, 'panos-view.html', context={
        'pano': pano,
        'is_detail_page': True,
        })

def categoria(request, categoria_id):
    panos = get_list_or_404(Panos.objects.filter(categoria__id=categoria_id, esta_publicado=True).order_by('-id'))
    return render(request, 'categoria.html', context={
        'panos': panos,
        'titulo': f'{panos[0].categoria.nome} - Categoria | ',
    })
