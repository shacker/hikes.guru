from django.conf.urls import url
from trails import views

urlpatterns = [
    url(r'^featured/$', views.featured, name='featured_trails'),
    url(r'^$', views.trails_list, name='trails_list'),
    url(r'^(?P<urlhash>[\w.-]+)/$', views.trail_detail, name='trail_detail'),
]
