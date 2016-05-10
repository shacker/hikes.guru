from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hikes.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Uploaded media in DEBUG mode
