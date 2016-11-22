from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy

from apps.campanha.models import Campanha
from .forms import CamForm


@login_required
def listar_campanhas(request):
    cam = Campanha.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(cam, 10)
    try:
        camp = paginator.page(page)
    except PageNotAnInteger:
        camp = paginator.page(1)
    except EmptyPage:
        camp = paginator.page(paginator.num_pages)

    return render(request, 'campanha/listar_campanhas.html', {'cam':camp})

@login_required
@permission_required('campanha.add_campanha')
def crear_campanha(request):
    if request.method == 'POST':
        form = CamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('campanha:listar_campanhas'))

    form = CamForm()
    context = {'form':form}
    return render(request, 'campanha/crear_campanha.html', context)

@login_required
@permission_required('campanha.change_campanha')
def modificar_campanha(request, campanha_id):

    campanha = Campanha.objects.get(pk=campanha_id)
    form = CamForm(instance=campanha)

    if request.method == 'POST':
        form = CamForm(request.POST, instance=campanha)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('campanha:listar_campanhas'))

    context = {'form':form, 'campanha_id':campanha_id}
    return render(request, 'campanha/modificar_campanha.html', context)

@login_required
@permission_required('campanha.remove_campanha')
def eliminar_campanha(request, id):
    cam = Campanha.objects.get(pk=id)
    cam.delete()
    return HttpResponseRedirect(reverse_lazy('campanha:listar_campanhas'))

@login_required
def listar_detalle_Cam(request, campanha_id):
    cam = Campanha.objects.all().get(pk=campanha_id)

    return render(request, 'campanha/listar_detalle_cam.html', {'cam':cam})



