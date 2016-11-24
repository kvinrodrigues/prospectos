from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from apps.campanha.models import Campanha
from apps.target.models import Target


def gestion_de_Ventas(request):
    listacam = Campanha.objects.all().order_by('pk')
    page = request.GET.get('page')
    paginator = Paginator(listacam, 10)
    try:
        listaCam = paginator.page(page)
    except PageNotAnInteger:
        listaCam = paginator.page(1)
    except EmptyPage:
        listaCam = paginator.page(paginator.num_pages)






    target =   Target.objects.all().order_by('pk')
    page1 = request.GET.get('page1')
    paginator = Paginator(target, 10)
    try:
        Tg = paginator.page(page1)
    except PageNotAnInteger:
        Tg = paginator.page(1)
    except EmptyPage:
        Tg = paginator.page(paginator.num_pages)
    context = {'Tg': Tg, 'listaCam': listaCam}
    return render(request, 'ventas/gestion_de_ventas.html', context)