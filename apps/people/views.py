import bleach

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils import timezone

from people.forms import ProfileEditForm, ContactForm
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
    trails = person.trail_set.all().order_by('-updated')

    # Hide private trails from non-superusers
    if not person == request.user and not request.user.is_superuser:
        trails = trails.exclude(public=True)

    page = request.GET.get('page', 1)
    paginator = Paginator(trails, 25)  # Number of trails per page
    try:
        trails = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        trails = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        trails = paginator.page(paginator.num_pages)

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


@login_required
def avatar_edit(request):
    """
    Replace/crop your avatar
    """

    person = get_object_or_404(UserProfile, username=request.user.username)

    return render(request, 'people/avatar_edit.html', locals())


@login_required
def contact(request, recipient):
    """
    Allow users to contact one another.
    """

    recipient = UserProfile.objects.get(username=recipient)

    if request.method == "POST":

        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            body = bleach.clean(contact_form.cleaned_data['body'], strip=True, tags=[])
            sender = request.user
            timestamp = timezone.now()
            subject = 'Contact via hikes.guru: {s}'.format(s=contact_form.cleaned_data['subject'])
            from_email = request.user.email
            to_email = [recipient.email, ]

            ctx = {
                'sender': sender,
                'recipient': recipient,
                'body': body,
            }

            message = render_to_string('people/contact_email.txt', ctx)
            msg = EmailMessage(subject, message, from_email, to_email,)
            msg.send()

            messages.success(request, "Your message has been sent.")
            return redirect(reverse('profile_detail', kwargs={'username': recipient.username}))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        contact_form = ContactForm()

    return render(request, 'people/contact.html', locals(), )
