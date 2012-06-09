from django.core.urlresolvers import reverse
from django.db import models
from tmsutil.constants import YEAR_CHOICES

class Tutor(models.Model):
    """ The base class for a tutor
    """

    first_name = models.CharField(max_length=50, help_text="John")
    last_name = models.CharField(max_length=50, help_text="Smith")
    email_address = models.EmailField(max_length=75,
            help_text="johnsmith@example.com")
    phone_number = models.CharField(max_length=15, help_text="987-654-3210")
    grad_year = models.IntegerField(max_length=4, help_text="2012")
    tutoring_preference_from = models.IntegerField(max_length=2, choices=YEAR_CHOICES)
    tutoring_preference_to = models.IntegerField(max_length=2, choices=YEAR_CHOICES)
    subjects = models.CharField(max_length=50, help_text="Math, reading, spanish")
    added_on = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)
    note = models.TextField(blank=True,
            help_text="Any extra information you would like us to know?")

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_tutoring_pref(self):
        pref_from = self.tutoring_preference_from
        if pref_from == 0:
            pref_from = 'K'
        return "%s-%s" % (pref_from, self.tutoring_preference_to)

    def __unicode__(self):
        return self.get_full_name()

    def get_edit_url(self):
        return reverse('tutors.views.edit_tutor', args=[self.id])
