from django.template.defaultfilters import slugify
from django.db import models
from people.models import UserProfile


def get_gpx_path(instance, filename):
    """
    Clean the filename and determine the foldername to upload track files to.
    """

    parts = str(filename).split(".")
    return 'trackfiles/' + instance.owner.username + '/' + slugify(parts[0]) + '.' + parts[1]


TRAIL_TYPE_CHOICES = [
    ('loop', 'Loop'),
    ('tb', 'There and Back'),
    ('ow', 'One Way'),
]


class Trail(models.Model):
    '''
    Base trips and trails model.
    '''

    owner = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=120)
    region = models.CharField(max_length=120, help_text="e.g. Yosemite, CA", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    trackfile = models.FileField(upload_to=get_gpx_path, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True, help_text="Stored as meters")
    ascent = models.IntegerField(blank=True, null=True, help_text="Stored as meters")
    calories = models.SmallIntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    geocaches = models.BooleanField(default=False, help_text="Geocaches available on this trail")
    public = models.BooleanField(default=True, help_text="Visible to the world")
    featured = models.BooleanField(default=False, help_text="Editor picks")
    trail_type = models.CharField(max_length=6, choices=(TRAIL_TYPE_CHOICES), default="loop")

    def __str__(self):
        return '{o} - {t}'.format(o=self.owner, t=self.title)
