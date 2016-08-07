from django.shortcuts import render, redirect
from django.contrib.auth import load_backend, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.contrib import messages

from people.models import UserProfile


def home(request):
    return render(request, 'home.html', locals())


def faqs(request):
    return render(request, 'faqs.html', locals())


# Superusers only
@user_passes_test(lambda u: u.is_superuser)
def login_as_other(request, username):
    '''
    Allows superusers to log in as another user.
    '''

    # Log out the current user
    logout(request)

    newuser = UserProfile.objects.get(username=username)
    if newuser.is_active:
        # Since we don't know their pword, we can't call authenticate(), so we
        # mock its effect by setting the `backend` property manually.
        if not hasattr(newuser, 'backend'):
            for backend in settings.AUTHENTICATION_BACKENDS:
                if newuser == load_backend(backend).get_user(newuser.pk):
                    newuser.backend = backend
                    login(request, newuser)
                    break

        messages.success(request, "You are now logged in as {u}".format(u=username))
    else:
        messages.error(request, "Could not log in as {u}. User may be inactive".format(u=username))

    return redirect('/')
