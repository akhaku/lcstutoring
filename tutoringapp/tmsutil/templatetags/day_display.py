from django import template
from tmsutil.constants import DAY_CHOICES

register = template.Library()

def display_day(value):
    """ Displays the day (represented as a digit) as a string """
    try:
        num = int(value)
    except ValueError:
        return value
    ret = filter(lambda x: x[0]==num, DAY_CHOICES)
    if len(ret) != 1:
        return ""
    return ret[0][1]

register.filter('display_day', display_day)
