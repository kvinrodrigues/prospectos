from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from apps.vendedor.models import Supervisor
from .forms import SupervisorForm
def listar_supervisor(request):
    supervisor= Supervisor.objects.all().order_by('pk')
    return render(request, 'supervisor/listar_supervisores.html', {'supervisor':supervisor})

def crear_supervisor(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('supervisor:listar_supervisores'))

    form = SupervisorForm()
    context = {'form':form}
    return render(request, 'supervisor/crear_supervisores.html', context)

def modificar_supervisor(request, supervisor_id):
    supervisor= Supervisor.objects.get(pk=supervisor_id)
    form = SupervisorForm(instance=supervisor)

    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('supervisor:listar_supervisores'))

    context = {'form':form, 'supervisor_id':supervisor_id}
    return render(request, 'supervisor/modificar_supervisores.html', context)

@login_required
@permission_required('supervisor.remove_supervisor')
def eliminar_supervisor(request, id):
    super = Supervisor.objects.get(pk=id)
    super.delete()
    return HttpResponseRedirect(reverse_lazy('supervisor:listar_supervisores'))