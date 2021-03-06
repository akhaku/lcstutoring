from django.db import models
from django.contrib.auth.models import User
from tutees.models import Tutee
from tutors.models import Tutor
from tmsutil.constants import DAY_CHOICES, MATCH_LOCATION_CHOICES

class Match(models.Model):
    """ The base class for a match
    """
    tutor = models.ForeignKey(Tutor, related_name="match")
    tutee = models.ForeignKey(Tutee, related_name="match")
    matcher = models.ForeignKey(User)
    day = models.IntegerField(max_length=1, choices=DAY_CHOICES, null=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=15, choices=MATCH_LOCATION_CHOICES,
            blank=True)
    added_on = models.DateTimeField(blank=False)
    active = models.BooleanField(default=True)
    note = models.TextField(blank=True,
            help_text="Any extra information.")

    def __unicode__(self):
      return "%s and %s" % (self.tutor, self.tutee)
