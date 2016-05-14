from django.db import models
from people.models import UserProfile


FEEDBACK_TYPE_CHOICES = (
    (u'bug', u'Bug'),
    (u'ux', u'User Experience'),
    (u'suggestion', u'Suggestion'),
    (u'question', u'Question'),
    (u'other', u'Other'),
)


class Feedback(models.Model):
    '''
    Simple user feedback.
    '''

    author = models.ForeignKey(UserProfile)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()
    feedback_type = models.CharField(max_length=12, choices=FEEDBACK_TYPE_CHOICES, blank=True)

    def __str__(self):
        return '{a} - {s}'.format(a=self.author, s=self.subject)

    class Meta:
        verbose_name = "User feedback"
        verbose_name_plural = "User feedback"
