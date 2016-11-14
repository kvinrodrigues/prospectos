from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, permission_required

from apps.rol.forms import RolForm





@login_required
def crear_rol(request):
    if request.method == 'GET':
        form = RolForm()

    else:
        form = RolForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rol:listar_roles'))

    return render(request, 'rol/crear_rol.html', {'form': form})


@login_required
def modificar_rol(request, rol_id):
    rol = Group.objects.get(pk=rol_id)
    form = RolForm(instance=rol)

    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rol:listar_roles'))

    context = {'form': form, 'rol_id': rol_id}
    return render(request, 'rol/modificar_rol.html', context)


@login_required
def eliminar_rol(request, rol_id):
    rol = Group.objects.get(pk=rol_id)
    rol.delete()
    return HttpResponseRedirect(reverse('rol:listar_roles'))


@login_required
def listar_roles(request):
    lista_roles = Group.objects.all().order_by('name')
    context = {'lista_roles':lista_roles}
    return render(request, 'rol/listar_roles.html', context)
