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
from trails.utils import trails_list


def alltrails(request):
    """
    Main trails directory /finder
    """

    trails_qs = Trail.objects.filter(public=True).order_by('-updated')
    paginator, trails = trails_list(request, trails_qs)  # paginated result
    q = request.GET.get('q')

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

    if (not trail.public) and (not trail.owner == request.user):
        return HttpResponseForbidden()

    return render(request, 'trails/trail_detail.html', locals())


def trail_edit(request, urlhash=None):
    """
    If urlhash present, edit trail; else create new.
    """

    if urlhash:
        trail = get_object_or_404(Trail, urlhash=urlhash)
        if not trail.owner == request.user:
            return HttpResponseForbidden()
    else:
        trail = Trail(owner=request.user)

    if request.method == "POST":

        form = TrailEditForm(request.POST, instance=trail)
        if form.is_valid():
            trailobj = form.save(commit=False)
            trailobj.body = bleach.clean(form.cleaned_data['description'], strip=True, tags=settings.ALLOWED_TAGS)
            trailobj.directions = bleach.clean(form.cleaned_data['directions'], strip=True, tags=settings.ALLOWED_TAGS)
            trailobj.updated = timezone.now()
            trailobj.save()

            messages.success(request, "Your trail has been edited.")
            return redirect(reverse('trail_detail', kwargs={'urlhash': trailobj.urlhash}))
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
