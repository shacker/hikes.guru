from django.conf.urls import url
from people import views


urlpatterns = [
    url(r'^$', views.directory, name='people_directory'),
    url(r'^edit/$', views.profile_edit, name='profile_edit'),
    url(r'^(?P<username>[\w.-]+)/$', views.profile_detail, name='profile_detail'),
]
