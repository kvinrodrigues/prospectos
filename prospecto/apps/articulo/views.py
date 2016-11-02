from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.articulo.models import Articulo
from .forms import ArtForm
def listar_articulos(request):
    art= Articulo.objects.all().order_by('pk')
    return render(request, 'articulo/listar_articulos.html', {'art8':art})


def crear_articulo(request):

    if request.method == 'POST':
        form = ArtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulo:listar_articulos'))

    form = ArtForm()
    context = {'form':form}
    return render(request, 'articulo/crear_articulos.html', context)



