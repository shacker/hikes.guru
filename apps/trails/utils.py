from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings


def trails_list(request, trails):
    '''
    Paginated, faceted Trails list reusable between alltrails and mytrails views.
    Returns both 'paginator' (which is a wrapper for the trails queryset)
    and 'trails' which is one page-worth of trails.
    '''
    q = request.GET.get('q')
    if q:
        trails = trails.annotate(search=SearchVector('title', 'description', 'region')).filter(search=q)

    page = request.GET.get('page', 1)
    paginator = Paginator(trails, settings.NUM_TRAILS_PER_PAGE)  # Number of trails per page
    try:
        trails = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        trails = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        trails = paginator.page(paginator.num_pages)

    return paginator, trails
