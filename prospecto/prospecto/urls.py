"""prospecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.inicio.urls')),
    url(r'^inicio/', include('apps.inicio.urls', namespace='inicio')),
    url(r'^usuario/', include('apps.usuarios.urls', namespace='usuarios')),
    url(r'^target/', include('apps.target.urls', namespace='target')),
    url(r'^articulo/', include('apps.articulo.urls', namespace='articulo')),
    url(r'^campanha/', include('apps.campanha.urls', namespace='campanha')),
    url(r'^history/', include('apps.history.urls', namespace='history')),
    url(r'^rol/', include('apps.rol.urls', namespace='rol')),
    url(r'^supervisor/', include('apps.supervisor.urls', namespace='supervisor')),
    url(r'^target_contact/', include('apps.target_contact.urls', namespace='target_contact')),
    url(r'^vendedor/', include('apps.vendedor.urls', namespace='vendedor')),
    url(r'^auditoria/', include('apps.auditoria.urls', namespace='auditoria')),



]
