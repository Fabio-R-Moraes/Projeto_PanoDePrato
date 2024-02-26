from django.shortcuts import render
from utils.fabrica import make_recipe

def home(request):
    return render(request, 'home.html', context={
        'panos': [make_recipe() for _ in range(10)],
    })

def pano(request, id):
    return render(request, 'panos-view.html', context={
        'pano': make_recipe(),
        'is_detail_page': True,
        })
