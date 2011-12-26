from django.db import models

class Tutor(models.Model):
    """ The base class for a tutor
    """

    _year_choices = (('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10','10'),
            ('11','11'),
            ('12','12'))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=75)
    phone_number = models.CharField(max_length=15)
    grad_year = models.IntegerField(max_length=4)
    tutoring_preference_from = models.IntegerField(max_length=2,
            choices=_year_choices)
    tutoring_preference_to = models.IntegerField(max_length=2,
            choices=_year_choices)
    subjects = models.CharField(max_length=50)
    note = models.TextField(blank=True)
