from django.conf.urls import url
from apps.target_contact import views

urlpatterns = [
    url(r'^$', views.listar_contacto, name='listar_contacto'),

    url(r'^listar_contacto/', views.listar_contacto, name='listar_contacto'),

    url(r'^crear_contacto/', views.crear_contacto, name='crear_contacto'),

    url(r'^modificar_contacto/(?P<contacto_id>\d+)/$', views.modificar_contacto, name='modificar_contacto'),

    url(r'^eliminar_contacto/(?P<id>\d+)/$', views.eliminar_contacto, name='eliminar_contacto')




]
