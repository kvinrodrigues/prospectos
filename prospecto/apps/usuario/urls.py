from django.conf.urls import url
from apps.usuario import views

urlpatterns = [

    url(r'^$', views.listar_usuario, name='listar_usuario'),
    # ej: usuario/crear_usuario
    url(r'^crear_usuarios/$', views.crear_usuario, name='crear_usuarios'),

    # ej: usuario/modificar_usuario/3
    url(r'^modificar_usuarios/(?P<usuario_id>\d+)/$', views.modificar_usuario, name='modificar_usuarios'),

    # ej: usuario/ eliminar_usuario/4
    #url(r'^eliminar_usuarios/(?P<usuario_id>\d+)/$', views.eliminar_usuario, name='eliminar_usuarios'),

    # ej: usuario/listar_usuario
    url(r'^listar_usuarios/$', views.listar_usuario, name='listar_usuarios')

]
