from django.conf.urls import  url
from apps.inicio import views

urlpatterns = [

	# ej: inicio/
	url(r'^$', views.autenticar, name='autenticar'),

	# ej: inicio/menu
	url(r'^menu/$', views.menu, name='menu'),

	url(r'^salir/$', views.salir, name='salir')

]



