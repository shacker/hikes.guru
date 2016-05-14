from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout

from hikes.views import home

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),  # social_auth
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),

    url(r'^admin/', admin.site.urls),
    url(r'^$', home),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Uploaded media in DEBUG mode
