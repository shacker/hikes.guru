from django.conf.urls import url
from people import views


urlpatterns = [

    url(r'^$', views.directory, name='people_directory'),
    url(r'^(?P<username>[\w.-]+)/$', views.profile_detail, name='profile_detail'),

]
