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
    subjects = models.CharField(max_length=50, help_text="Math, Reading, Writing")
    note = models.TextField(blank=True,
            help_text="Any extra information you would like us to know?")
