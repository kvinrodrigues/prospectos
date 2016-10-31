from django.conf.urls import include, url
from apps.usuarios import views
urlpatterns = [
        url(r'^$', views.post_list),
]