from django.db import models

class AppSetting(models.Model):
    """ The base class for a setting
        The following are the app-specific settings with their IDs:
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)
    value = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s" % (name, value)
