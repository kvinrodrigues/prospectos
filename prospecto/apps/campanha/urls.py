from django.conf.urls import url
from apps.campanha import views

urlpatterns = [
    url(r'^$', views.listar_campanhas, name='listar_campanhas'),

    url(r'^listar_campanhas/', views.listar_campanhas, name='listar_campanhas'),

    url(r'^crear_campanha/', views.crear_campanha, name='crear_campanha'),

    url(r'^modificar_campanha/(?P<campanha_id>\d+)/$', views.modificar_campanha, name='modificar_campanha'),

    url(r'^eliminar_campanha/(?P<id>\d+)/$', views.eliminar_campanha, name='eliminar_campanha')




]
