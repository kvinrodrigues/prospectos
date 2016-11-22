from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.articulo.models import Articulo
from .forms import ArtForm


@login_required
def listar_articulo(request):
    arte = Articulo.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(arte, 10)
    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        art = paginator.page(1)
    except EmptyPage:
        art = paginator.page(paginator.num_pages)

    return render(request, 'articulo/listar_articulos.html', {'art': art})

@login_required
@permission_required('articulo.add_articulos')
def crear_articulo(request):
    if request.method == 'POST':
        form = ArtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulo:listar_articulos'))

    form = ArtForm()
    context = {'form': form}
    return render(request, 'articulo/crear_articulos.html', context)


@login_required
@permission_required('articulo.change_articulo')
def modificar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    form = ArtForm(instance=articulo)

    if request.method == 'POST':
        form = ArtForm(request.POST, instance=articulo)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articulo:listar_articulos'))

    context = {'form': form, 'articulo_id': articulo_id}
    return render(request, 'articulo/modificar_articulos.html', context)


@login_required
@permission_required('articulo.remove_articulo')
def eliminar_articulo(request, id):
    arti = Articulo.objects.get(pk=id)
    arti.delete()
    return HttpResponseRedirect(reverse_lazy('articulo:listar_articulos'))



@login_required
def listar_detallearti(request, id):
    arte = Articulo.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(arte, 10)
    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        art = paginator.page(1)
    except EmptyPage:
        art = paginator.page(paginator.num_pages)

    return render(request, 'articulo/listar_detalleart.html', {'art': art})