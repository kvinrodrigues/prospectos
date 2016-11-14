from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Target
from .forms import TargetForm
def listar_target(request):
    target= Target.objects.all().order_by('pk')
    return render(request, 'target/listar_targets.html', {'target':target})

def crear_target(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target:listar_targets'))

    form = TargetForm()
    context = {'form':form}
    return render(request, 'target/crear_targets.html', context)

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