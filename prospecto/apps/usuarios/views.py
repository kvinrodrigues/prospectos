from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required, permission_required

from .forms import UsuarioModelForm, CrearUsuarioModelForm

@login_required
@permission_required('auth.add_user')
def crear_usuario(request):
    if request.method == 'GET':
        form = CrearUsuarioModelForm()

    else:
        form = CrearUsuarioModelForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.clean_password2()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            groups = form.cleaned_data['groups']
            is_active = form.cleaned_data['is_active']

            usuario = User.objects.create(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_active=is_active,
                is_staff=True,
            )
            usuario.set_password(password)
            for g in groups:
                usuario.groups.add(g)
            usuario.save()
            return HttpResponseRedirect(reverse('usuarios:listar_usuarios'))

    return render(request, 'usuario/crear_usuarios.html', {'form': form})

@login_required
@permission_required('auth.change_user')
def modificar_usuario(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    form = UsuarioModelForm(instance=usuario)

    if request.method == 'POST':
        form = UsuarioModelForm(request.POST, instance=usuario)

        if form.is_valid():
            username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            groups = form.cleaned_data['groups']
            is_active = form.cleaned_data['is_active']

            usuario.username = username
            # usuario.password = password
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.email = email
            usuario.groups.clear()
            for g in groups:
                usuario.groups.add(g)
            usuario.is_active = is_active
            usuario.save()

            return HttpResponseRedirect(reverse('usuarios:listar_usuarios'))

    context = {'form': form, 'usuario_id': usuario_id}
    return render(request, 'usuario/modificar_usuarios.html', context)


@login_required
@permission_required('auth.delete_user')
def eliminar_usuario(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    usuario.delete()
    return HttpResponseRedirect(reverse('usuarios:listar_usuarios'))


@login_required
@permission_required('auth.change_user')
def listar_usuario(request):
    lista_user = User.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(lista_user, 10)
    try:
        lista_usuarios = paginator.page(page)
    except PageNotAnInteger:
        lista_usuarios = paginator.page(1)
    except EmptyPage:
        lista_usuarios = paginator.page(paginator.num_pages)


    return render(request, 'usuario/listar_usuarios.html', {'lista_usuarios': lista_usuarios})
