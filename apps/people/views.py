import bleach

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from people.forms import ProfileEditForm
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


@login_required
def profile_edit(request):
    """
    Edit your own profile.
    """

    profile = UserProfile.objects.get(username=request.user.username)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            new_data = form.save(commit=False)
            about = bleach.clean(form.cleaned_data['about'], strip=True, tags=settings.ALLOWED_TAGS)
            new_data.about = about
            new_data.save()

            messages.success(request, "Profile edited successfully.")
            return redirect(reverse('profile_detail', kwargs={'username': request.user.username}))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'people/profile_edit.html', locals(), )
