from django.conf.urls import url
from apps.usuarios import views
urlpatterns = [
        url(r'^$', views.post_list)
]