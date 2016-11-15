from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy


def listar_auditoria(request):

    return render(request, 'auditoria/listar_auditoria.html', {})
