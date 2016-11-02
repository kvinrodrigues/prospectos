from django.conf.urls import url
from apps.articulo import views

urlpatterns = [
    url(r'^$', views.listar_articulo, name='listar_articulos'),
    # ej: proyecto/listar_proyectos
    url(r'^listar_articulos/', views.listar_articulo, name='listar_articulos'),
    # ej: articulo/crear_articulo
    url(r'^crear_articulos/', views.crear_articulo, name='crear_articulos')]


