from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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



