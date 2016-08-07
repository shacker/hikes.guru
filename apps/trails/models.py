from django.db import models
from django.template.defaultfilters import slugify

from base.utils import id_generator
from base.choices import COUNTRIES_CHOICES
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

ACTIVITY_TYPE_CHOICES = [
    ('hike', 'Hike/Walk'),
    ('bike', 'Bike'),
]

DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('mod', 'Moderate'),
    ('hard', 'Strenuous'),
]

SEASON_CHOICES = [
    ('all', 'Year-Round'),
    ('mild', 'Spring Through Fall'),
]


class Trail(models.Model):
    '''
    Base trips and trails model.
    '''

    urlhash = models.CharField(max_length=6, null=True, blank=True, unique=True, default=None)
    owner = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=120)
    country = models.CharField(max_length=2, choices=(COUNTRIES_CHOICES), default="US")
    region = models.CharField(max_length=120, help_text="e.g. 'Yosemite' or 'New York'")
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    trackfile = models.FileField(upload_to=get_gpx_path, blank=True, null=True)
    distance = models.PositiveIntegerField(blank=True, null=True, help_text="Stored as meters")
    ascent = models.IntegerField(blank=True, null=True, help_text="Stored as meters")
    calories = models.PositiveSmallIntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    geocaches = models.BooleanField(default=False, help_text="Geocaches available on this trail")
    public = models.BooleanField(default=True, help_text="Visible to the world")
    featured = models.BooleanField(default=False, help_text="Editor picks")
    trail_type = models.CharField(max_length=6, choices=(TRAIL_TYPE_CHOICES), default="loop")
    activity_type = models.CharField(max_length=6, choices=(ACTIVITY_TYPE_CHOICES), default="hike")
    difficulty = models.CharField(max_length=6, choices=(DIFFICULTY_CHOICES), default="mod")
    season = models.CharField(max_length=6, choices=(SEASON_CHOICES), default="all")
    directions = models.TextField("Driving or Trail Directions", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Make sure all trails get a urlhash, regardless how they're saved.
        if not self.urlhash:
            self.urlhash = id_generator()
            while Trail.objects.filter(urlhash=self.urlhash).exists():
                self.urlhash = id_generator()
        super(Trail, self).save(*args, **kwargs)

    def __str__(self):
        return '{o} - {t}'.format(o=self.owner, t=self.title)
