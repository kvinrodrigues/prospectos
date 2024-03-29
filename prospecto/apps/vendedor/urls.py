from django.conf.urls import url
from apps.vendedor import views

urlpatterns = [
    url(r'^$', views.listar_vendedor, name='listar_vendedores'),
    url(r'^listar_vendedores/', views.listar_vendedor, name='listar_vendedores'),
    url(r'^crear_vendedores/', views.crear_vendedor, name='crear_vendedores'),
    url(r'^modificar_vendedor/(?P<vendedor_id>\d+)/$', views.modificar_vendedor, name='modificar_vendedor',),
    url(r'^eliminar_vendedores/(?P<id>\d+)/$', views.eliminar_vendedor, name='eliminar_vendedores'),
    url(r'^listar_detalles/(?P<vendedor_id>\d+)/$', views.listar_detalle, name='listar_detalles')

]
