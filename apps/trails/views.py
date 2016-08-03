import bleach
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from trails.models import Trail
from trails.forms import TrailEditForm


def trails_list(request):
    """
    Main trails directory /finder
    """

    trails = Trail.objects.all().order_by('-updated')

    return render(request, 'trails/list.html', locals())


def featured(request):
    """
    Trails featured by editors
    """

    trails = Trail.objects.filter(featured=True)

    return render(request, 'trails/featured.html', locals())


def trail_detail(request, urlhash):
    """
    Single trail detail view
    """

    trail = get_object_or_404(Trail, urlhash=urlhash)
    return render(request, 'trails/trail_detail.html', locals())


def trail_edit(request, urlhash):
    """
    Single trail edit view
    """

    trail = get_object_or_404(Trail, urlhash=urlhash)

    if not trail.owner == request.user:
        return HttpResponseForbidden()

    if request.method == "POST":

        form = TrailEditForm(request.POST, instance=trail)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.body = bleach.clean(form.cleaned_data['description'], strip=True, tags=settings.ALLOWED_TAGS)
            updated.updated = timezone.now()
            updated.save()

            messages.success(request, "Your trail has been edited.")
            return redirect(reverse('trail_detail', kwargs={'urlhash': urlhash}))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        form = TrailEditForm(instance=trail)

    return render(request, 'trails/trail_edit.html', locals())


@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def toggle_featured(request):
    '''
    Superuser can toggle a trail's "featured" status via ajax.
    '''

    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode('utf-8'))
        urlhash = received_json_data.get('urlhash', None)
        trail = Trail.objects.get(urlhash=urlhash)
        if trail.featured:
            trail.featured = False
        else:
            trail.featured = True
        trail.save()

        return HttpResponse(status=204)


@csrf_exempt
def toggle_bookmark(request):
    '''
    User can toggle a trail's "bookmarked" status via ajax.
    '''

    if request.method == 'POST' and request.user.is_authenticated():
        received_json_data = json.loads(request.body.decode('utf-8'))
        urlhash = received_json_data.get('urlhash', None)
        trail = Trail.objects.get(urlhash=urlhash)
        bookmarks = request.user.bookmarks

        if trail in bookmarks.all():
            bookmarks.remove(trail)
        else:
            bookmarks.add(trail)

    return HttpResponse(status=204)
