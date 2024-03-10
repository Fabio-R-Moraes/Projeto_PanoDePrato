from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Panos
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from utils.paginacao import make_pagination_range

def home(request):
    panos = Panos.objects.filter(esta_publicado=True).order_by('-id')

    try:
        pagina_atual = int(request.GET.get('page', 1))
    except ValueError:
        pagina_atual = 1

    paginador = Paginator(panos, 6)
    pagina_objeto = paginador.get_page(pagina_atual)
    range_paginacao = make_pagination_range(
        paginador.page_range,
        4,
        pagina_atual,
    )

    return render(request, 'home.html', context={
        'panos': pagina_objeto,
        'range_paginacao': range_paginacao,
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

def procurar(request):
    termo_procurado = request.GET.get('q','').strip()

    if not termo_procurado:
        raise Http404()
    
    panos = Panos.objects.filter(
        Q(
            Q(titulo__icontains=termo_procurado) | 
            Q(descricao__icontains=termo_procurado),
        ),
        esta_publicado=True,
    ).order_by('-titulo')

    return render(request, 'procurar.html', {
        'page_title': f'Pesquisando por "{termo_procurado}" |', 
        'panos': panos,
    })
