from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from apps.articulo.models import Articulo
from .forms import ArtForm

@login_required
def listar_articulo(request):
    art= Articulo.objects.all().order_by('pk')
    return render(request, 'articulo/listar_articulos.html', {'art':art})

@login_required
@permission_required('articulo.crear_articulos')
def crear_articulo(request):
    if request.method == 'POST':
        form = ArtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulo:listar_articulos'))

    form = ArtForm()
    context = {'form':form}
    return render(request, 'articulo/crear_articulos.html', context)



