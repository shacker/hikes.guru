import json

from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from trails.models import Trail


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
