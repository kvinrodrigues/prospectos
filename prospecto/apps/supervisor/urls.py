from django.conf.urls import url
from apps.supervisor import views

urlpatterns = [
    url(r'^$', views.listar_supervisor, name='listar_supervisores'),
    url(r'^listar_supervisores/', views.listar_supervisor, name='listar_supervisores'),
    url(r'^crear_supervisores/', views.crear_supervisor, name='crear_supervisores'),
    url(r'^modificar_supervisores/(?P<supervisor_id>\d+)/$', views.modificar_supervisor, name='modificar_supervisores'),
    url(r'^eliminar_supervisores/(?P<id>\d+)/$', views.eliminar_supervisor, name='eliminar_supervisores')
]
