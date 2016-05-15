from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout
from django.views.generic.base import RedirectView


from hikes.views import home
from feedback.views import feedback


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),

    url('', include('social.apps.django_app.urls', namespace='social')),  # social_auth
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^feedback/$', feedback, name='feedback'),
    url(r'^people/', include('people.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Uploaded media in DEBUG mode
