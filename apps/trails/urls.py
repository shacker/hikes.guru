from django.conf.urls import url
from trails import views

urlpatterns = [
    url(r'^(?P<urlhash>[\w.-]+)/$', views.trail_detail, name='trail_detail'),
    url(r'^featured/$', views.featured, name='featured_trails'),
]
