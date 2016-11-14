from django.conf.urls import url
from apps.rol import views

urlpatterns = [

    url(r'^crear_rol/$', views.crear_rol, name='crear_rol'),

    url(r'^modificar_rol/(?P<rol_id>\d+)/$', views.modificar_rol, name='modificar_rol'),

    url(r'^eliminar_rol/(?P<rol_id>\d+)/$', views.eliminar_rol, name='eliminar_rol'),

    url(r'^listar_roles/', views.listar_roles, name='listar_roles'),

]
