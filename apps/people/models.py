from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField


def get_avatar_path(instance, filename):
    """
    Clean the filename and determine the foldername to upload avatars to.
    Must be defined before the Profile class.
    """

    parts = str(filename).split(".")
    return 'avatars/' + instance.username + '/' + slugify(parts[0]) + '.' + parts[1]


def validate_username(username):
    if " " in username:
        msg = 'Usernames cannot contain spaces'
        raise ValidationError(msg)


DISTANCE_CHOICES = [
    ('km', 'kilometers'),
    ('mi', 'miles'),
]


class UserProfile(AbstractUser):
    """
    Custom user/profile class, inheriting from Django's native auth.models.User.
    """

    about = models.TextField(
        help_text='Describe yourself: Interests, Bio, etc. Limited to 500 words.', null=True, blank=True)
    twitter = models.CharField(
        max_length=60, help_text='Your Twitter username',
        null=True, blank=True, validators=[validate_username, ])
    facebook = models.CharField(
        max_length=60, help_text='Your Facebook username',
        null=True, blank=True, validators=[validate_username, ])
    instagram = models.CharField(
        max_length=60, help_text='Your Instagram username',
        null=True, blank=True, validators=[validate_username, ])
    photo = ImageField(upload_to=get_avatar_path, blank=True, null=True, max_length=255)
    distance_pref = models.CharField(max_length=2, choices=(DISTANCE_CHOICES), default="mi")
    hide_real_name = models.BooleanField(
        default=False, help_text='If checked, username will be shown in place of First/Last')

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.username if self.hide_real_name else self.full_name
