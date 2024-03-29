from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import Target_ContactForm
from .models import Target_Contact


@login_required
def listar_contacto(request):
    contacto = Target_Contact.objects.all().order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(contacto, 10)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)

    return render(request, 'target_contact/listar_contacto.html', {'contact': contact})


@login_required
@permission_required('target_contact.add_target_contact')
def crear_contacto(request):
    if request.method == 'POST':
        form = Target_ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target_contact:listar_contacto'))

    form = Target_ContactForm()
    context = {'form': form}
    return render(request, 'target_contact/crear_contacto.html', context)


@login_required
@permission_required('target_contact.change_target_contact')
def modificar_contacto(request, contacto_id):
    target = Target_Contact.objects.get(pk=contacto_id)
    form = Target_ContactForm(instance=target)

    if request.method == 'POST':
        form = Target_ContactForm(request.POST, instance=target)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target:listar_targets'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'target_contact/modificar_contacto.html', context)


@login_required
@permission_required('target_contact.remove_target_contact')
def eliminar_contacto(request, id):
    tc = Target_Contact.objects.get(pk=id)
    tc.delete()
    return HttpResponseRedirect(reverse_lazy('target_contact:listar_contacto'))
