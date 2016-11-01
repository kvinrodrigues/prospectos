from django.shortcuts import render
from .models import Articulo
def listar_art(request):
    art= Articulo.objects.all().order_by('pk')
    return render(request, 'articulo/listar_articulos.html', {'art':art})