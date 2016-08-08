from django.conf.urls import url
from trails import views

urlpatterns = [
    url(r'^featured/$', views.featured, name='featured_trails'),
    url(r'^toggle_featured/$', views.toggle_featured, name='toggle_featured'),
    url(r'^toggle_bookmark/$', views.toggle_bookmark, name='toggle_bookmark'),
    url(r'^$', views.alltrails, name='alltrails'),
    url(r'^(?P<urlhash>[\w.-]+)/edit/$', views.trail_edit, name='trail_edit'),
    url(r'^new/$', views.trail_edit, name='trail_new'),
    url(r'^(?P<urlhash>[\w.-]+)/$', views.trail_detail, name='trail_detail'),
]
