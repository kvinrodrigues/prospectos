from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from apps.vendedor.models import Vendedor
from .forms import VendedorForm
def listar_vendedor(request):
    vende= Vendedor.objects.all().order_by('pk')
    return render(request, 'vendedor/listar_vendedores.html', {'vende':vende})

def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vendedor:listar_vendedores'))

    form = VendedorForm()
    context = {'form':form}
    return render(request, 'vendedor/crear_vendedores.html', context)



