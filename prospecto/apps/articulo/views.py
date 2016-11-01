from django.shortcuts import render
from .models import Articulo
def listar_art(request):
    return render(request, 'articulo/listar_articulos.html', {'Articulo':Articulo})