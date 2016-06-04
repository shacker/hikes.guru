from django.shortcuts import get_object_or_404, render

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
