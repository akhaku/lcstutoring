from django.db import models

class Tutor(models.Model):
    """ The base class for a tutor
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=75)
