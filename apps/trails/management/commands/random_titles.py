from django.core.management.base import BaseCommand
import random

from trails.models import Trail


class Command(BaseCommand):
    '''
    Randomly rewrite titles and regions of all trails. Dangerous!
    '''

    def handle(self, *args, **options):

        word_file = "/usr/share/dict/words"
        WORDS = open(word_file).read().splitlines()

        city_file = "/Users/shacker/dev/hikes.guru/apps/trails/management/commands/US_Cities.txt"
        CITIES = open(city_file).read().splitlines()

        trails = Trail.objects.all()

        for trail in trails:
            numwords = random.randint(2, 8)
            random_words = random.sample(WORDS, numwords)
            newtitle = " ".join(random_words)
            newtitle = newtitle[0].upper()+newtitle[1:]

            numwords = random.randint(2, 8)
            random_words = random.sample(WORDS, numwords)
            newtitle = " ".join(random_words)
            newtitle = newtitle[0].upper()+newtitle[1:]

            newregion = random.sample(CITIES, 1)[0]

            trail.title = newtitle
            trail.region = newregion
            trail.save()
