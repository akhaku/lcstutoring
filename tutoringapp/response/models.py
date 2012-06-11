from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

class Response(models.Model):
    """ The base class for a response
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name your response")
    description = models.CharField(max_length=255, help_text="Describe this response")
    response = models.TextField(blank=True,
            help_text="Response")
    created_by = models.ForeignKey(User)
    last_updated = models.DateTimeField(blank=False)

    def get_edit_url(self):
        return reverse('response.views.edit_response', args=[self.id])

    def get_delete_url(self):
        return reverse('response.views.delete_response', args=[self.id])
