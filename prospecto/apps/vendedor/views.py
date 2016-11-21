from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from apps.vendedor.models import Vendedor
from .forms import VendedorForm
@login_required
@permission_required('vendedor.add_vendedor')
def listar_vendedor(request):
    vende= Vendedor.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(vende, 10)
    try:
        vendes = paginator.page(page)
    except PageNotAnInteger:
        vendes = paginator.page(1)
    except EmptyPage:
        vendes = paginator.page(paginator.num_pages)

    return render(request, 'vendedor/listar_vendedores.html', {'vende':vendes})
@login_required
@permission_required('vendedor.add_vendedor')
def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vendedor:listar_vendedores'))

    form = VendedorForm()
    context = {'form':form}
    return render(request, 'vendedor/crear_vendedores.html', context)

@login_required
@permission_required('vendedor.change_vendedor')
def modificar_vendedor(request, vendedor_id):

    vendedor = Vendedor.objects.get(pk=vendedor_id)
    form = VendedorForm(instance=vendedor)

    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vendedor:listar_vendedores'))

    context = {'form':form, 'vendedor_id':vendedor_id}
    return render(request, 'vendedor/modificar_vendedores.html', context)

@login_required
@permission_required('vendedor.delete_vendedor')
def eliminar_vendedor(request, id):
    vend = Vendedor.objects.get(pk=id)
    vend.delete()
    return HttpResponseRedirect(reverse_lazy('vendedor:listar_vendedores'))

