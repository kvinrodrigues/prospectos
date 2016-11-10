from django.conf.urls import url
from apps.articulo import views

urlpatterns = [
    url(r'^$', views.listar_articulo, name='listar_articulos'),
    # listar articulo
    url(r'^listar_articulos/', views.listar_articulo, name='listar_articulos'),
    # crear articulo
    url(r'^crear_articulos/', views.crear_articulo, name='crear_articulos'),
    #modificar articulo
    url(r'^modificar_articulo/(?P<articulo_id>\d+)/$', views.modificar_articulo, name='modificar_articulo'),

    url(r'^eliminar_articulo/(?P<id>\d+)/$', views.eliminar_articulo, name='eliminar_articulo')




]


