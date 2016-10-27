from django.conf.urls import include, url
from vlog import views
urlpatterns = [
        url(r'^$', views.post_list),
]