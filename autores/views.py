from django.shortcuts import render
from autores.forms import RegistroForm

def registro_view(request):
    if request.POST:
        formulario = RegistroForm(request.POST)
    else:
        formulario = RegistroForm()

    return render(request, 'registro_view.html', {
        'form': formulario,
    })
