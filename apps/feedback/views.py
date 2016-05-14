import bleach

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone

from feedback.forms import FeedbackForm


@login_required
def feedback(request):
    """
    Gather user feedback and suggestions.
    Save record and send mail to site admins.
    """

    if request.method == "POST":

        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            body = bleach.clean(feedback_form.cleaned_data['body'], strip=True, tags=[])
            new_data = feedback_form.save(commit=False)
            new_data.body = body
            new_data.author = request.user
            new_data.timestamp = timezone.now()
            new_data.save()

            subject = 'hikes.guru feedback: {s}'.format(s=feedback_form.cleaned_data['subject'])
            from_email = request.user.email
            to_email = [addr[1] for addr in settings.ADMINS]

            ctx = {
                'user': request.user,
                'body': body,
                'feedback_type': new_data.get_feedback_type_display()
            }

            message = render_to_string('feedback/email.txt', ctx)
            msg = EmailMessage(subject, message, to=to_email, from_email=from_email)
            msg.send()

            messages.success(request, "Thanks for the feedback!")
            return redirect(reverse('home'))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        feedback_form = FeedbackForm(initial={'feedback_type': 'suggestion'})

    return render(request, 'feedback/feedback.html', locals(), )
