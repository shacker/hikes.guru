from django import template
from base.utils import meters_to_dist

register = template.Library()


@register.simple_tag
def meters_to_distance(meters, pref, format="long"):
    '''
    Takes args `meters` (int) and `pref` ('mi' or 'km'),
    returns float in miles or kilometers. Usage:
    {% meters_to_dist 8736433 "mi" %}
    If format == "short", returns in feet or meters.
    '''

    if meters:
        dist = meters_to_dist(meters, pref, format)
        rounded_dist = round(dist, 2)
        if format == "long" and pref == "mi":
            units = "miles"
        elif format == "short" and pref == "mi":
            units = "feet"
        elif format == "long" and pref == "km":
            units = "km"
        else:
            # format = "short" and pref = "km"
            units = "meters"

        return "{d} {u}".format(d=rounded_dist, u=units)
    else:
        return None
