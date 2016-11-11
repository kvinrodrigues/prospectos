from django.conf.urls import url
from apps.usuarios import views

urlpatterns = [

    url(r'^$', views.listar_usuario, name='listar_usuario'),



    # ej: usuario/modificar_usuario/3
    url(r'^modificar_usuarios/(?P<usuario_id>\d+)/$', views.modificar_usuario, name='modificar_usuarios'),

    # ej: usuario/crear_usuario
    url(r'^crear_usuarios/', views.crear_usuario, name='crear_usuarios'),

    url(r'^eliminar_usuario/(?P<usuario_id>\d+)/$', views.eliminar_usuario, name='eliminar_usuario'),

    # ej: usuario/listar_usuario
    url(r'^listar_usuarios/$', views.listar_usuario, name='listar_usuarios')

]
