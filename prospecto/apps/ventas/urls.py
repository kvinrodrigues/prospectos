from django.conf.urls import url
from apps.ventas import views

urlpatterns = [

    url(r'^$', views.gestion_de_Ventas, name='gestion_de_ventas'),
    url(r'^gestion_de_ventas/', views.gestion_de_Ventas, name='gestion_de_ventas'),
]
