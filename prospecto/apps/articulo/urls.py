from django.conf.urls import patterns, url
from apps.articulo import views

urlpatterns = patterns('',

		url(r'^$', views.listar_art, name='listar_art'),

)