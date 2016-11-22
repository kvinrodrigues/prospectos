from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Target
from .forms import TargetForm

@login_required
def listar_target(request):
    targe= Target.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(targe, 10)
    try:
        target = paginator.page(page)
    except PageNotAnInteger:
        target = paginator.page(1)
    except EmptyPage:
        target = paginator.page(paginator.num_pages)

    return render(request, 'target/listar_targets.html', {'target':target})

@login_required
@permission_required('target.add_target')
def crear_target(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target:listar_targets'))

    form = TargetForm()
    context = {'form':form}
    return render(request, 'target/crear_targets.html', context)

@login_required
@permission_required('target.change_target')
def modificar_target(request, target_id):
    target= Target.objects.get(pk=target_id)
    form = TargetForm(instance=target)

    if request.method == 'POST':
        form = TargetForm(request.POST, instance=target)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target:listar_targets'))

    context = {'form':form, 'target_id':target_id}
    return render(request, 'target/modificar_targets.html', context)

@login_required
@permission_required('target.remove_target')
def eliminar_target(request, id):
    target = Target.objects.get(pk=id)
    target.delete()
    return HttpResponseRedirect(reverse_lazy('target:listar_targets'))

@login_required
def listar_detalles_Tg(request, target_id):
    target= Target.objects.get(pk=target_id)

    return render(request, 'target/listar_detalles_tg.html', {'target':target})
