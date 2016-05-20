from django.shortcuts import render
from trails.models import Trail

def featured(request):
    """
    Trails featured by editors
    """

    trails = Trail.objects.filter(featured=True)

    return render(request, 'trails/featured.html', locals())
