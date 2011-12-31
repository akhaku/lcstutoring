from django.db import models
from tmsutil.constants import YEAR_CHOICES

class Tutee(models.Model):
    """ The base class for a tutee
    """
    parent_first_name = models.CharField(max_length=50, help_text="Jack")
    parent_last_name = models.CharField(max_length=50, help_text="Smith")
    child_first_name = models.CharField(max_length=50, help_text="Jill")
    child_last_name = models.CharField(max_length=50, help_text="Smith")
    gender = models.CharField(max_length=6,
            choices=(('male','Male'),('female','Female')))
    email_address = models.EmailField(max_length=75, blank=True,
            help_text="johnsmith@example.com")
    home_phone_number = models.CharField(max_length=15, blank=True,
            help_text="987-654-3210")
    cell_phone_number = models.CharField(max_length=15, blank=True,
            help_text="987-654-3210")
    grade = models.IntegerField(max_length=2, choices = YEAR_CHOICES)
    subjects = models.CharField(max_length=50, help_text="Math, Reading, Writing")
    note = models.TextField(blank=True,
            help_text="Any extra information you would like us to know?")

    def get_child_full_name(self):
        return "%s %s" % (self.child_first_name, self.child_last_name)

    def get_parent_full_name(self):
        return "%s %s" % (self.parent_first_name, self.parent_last_name)

