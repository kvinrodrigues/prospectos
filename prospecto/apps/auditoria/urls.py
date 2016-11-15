from django.conf.urls import url
from apps.auditoria import views

urlpatterns = [
    url(r'^$', views.listar_auditoria, name='listar_auditoria'),





]


