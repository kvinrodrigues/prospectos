from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import Target_ContactForm
from .models import Target_Contact



@login_required
def listar_contacto(request):
    contact= Target_Contact.objects.all().order_by('id')
    return render(request, 'target_contact/listar_contacto.html', {'contact':contact})

@login_required
@permission_required('target_contact.crear_contacto')
def crear_contacto(request):
    if request.method == 'POST':
        form = Target_ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('target_contact:listar_contacto'))

    form = Target_ContactForm()
    context = {'form':form}
    return render(request, 'target_contact/crear_contacto.html', context)

@login_required
@permission_required('contacto.modificar_contacto')
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
@permission_required('contacto.eliminar_contacto')
def eliminar_contacto(request, id):
    tc = Target_Contact.objects.get(pk=id)
    tc.delete()
    return HttpResponseRedirect(reverse_lazy('target_contact:listar_contacto'))