from django.conf.urls import url
from trails import views

urlpatterns = [
    url(r'^featured/$', views.featured, name='featured_trails'),
]
