from django.conf.urls import url
from apps.target import views

urlpatterns = [url(r'^$', views.listar_target, name='listar_targets'),
    url(r'^listar_targets/', views.listar_target, name='listar_targets'),
    url(r'^crear_targets/', views.crear_target, name='crear_targets'),
    url(r'^modificar_targets/(?P<target_id>\d+)/$', views.modificar_target, name='modificar_targets'),
    url(r'^eliminar_targets/(?P<id>\d+)/$', views.eliminar_target, name='eliminar_targets')

]