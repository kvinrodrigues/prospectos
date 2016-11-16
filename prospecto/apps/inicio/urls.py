from django.conf.urls import url
from apps.inicio import views

urlpatterns = [

    url(r'^$', views.autenticar, name='autenticar'),

    url(r'^menu/$', views.menu, name='menu'),
    url(r'^home/$', views.home, name='home'),

    url(r'^salir/$', views.salir, name='salir')

]
