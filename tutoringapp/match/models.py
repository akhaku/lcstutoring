from django.db import models
from django.contrib.auth.models import User
from tutee.models import Tutee
from tutor.models import Tutor
from tmsutil.constants import DAY_CHOICES, MATCH_LOCATION_CHOICES

class Match(models.Model):
    """ The base class for a match
    """
    tutor = models.ForeignKey(Tutor, related_name="match")
    tutee = models.ForeignKey(Tutee, related_name="match")
    matcher = models.ForeignKey(User)
    day = models.CharField(max_length=1, choices=DAY_CHOICES, blank=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=15, choices=MATCH_LOCATION_CHOICES,
            blank=True)
    added_on = models.DateTimeField(blank=False)
    active = models.BooleanField(default=True)
    note = models.TextField(blank=True,
            help_text="Any extra information.")

