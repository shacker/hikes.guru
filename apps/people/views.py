
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from people.models import UserProfile


def directory(request):

    """
    Browse / search / filter people.
    """
    people = UserProfile.objects.all()

    return render(request, 'people/directory.html', locals())


def profile_detail(request, username):
    """
    Display an individual profile
    """

    person = get_object_or_404(UserProfile, username=username)

    return render(request, 'people/profile_detail.html', locals())
