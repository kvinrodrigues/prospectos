from django.conf.urls import url
from apps.articulo import views

urlpatterns = [
    url(r'^$', views.listar_articulo, name='listar_articulos'),
    url(r'^listar_articulos/', views.listar_articulo, name='listar_articulos'),
    url(r'^crear_articulos/', views.crear_articulo, name='crear_articulos'),
    url(r'^modificar_articulos/(?P<articulo_id>\d+)/$', views.modificar_articulo, name='modificar_articulos'),
    url(r'^eliminar_articulos/(?P<id>\d+)/$', views.eliminar_articulo, name='eliminar_articulos'),
    url(r'^listar_detalleart/(?P<id>\d+)/$', views.listar_detallearti, name='listar_detalleart')
]


