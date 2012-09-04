from django.conf import settings
from django.contrib.auth.models import User
from match.models import Match
from response.models import Response
from tutees.models import Tutee
from tutors.models import Tutor
""" Utility methods
"""
def model_to_key(model):
    """ Serialize a model for notifications
    """
    assert model.id, "model must have an id"
    return "%s/%s" % (model.__class__.__name__, model.id)

def key_to_model(key):
    key = key.split('/')
    clazz = {'Tutor': Tutor,
            'Tutee': Tutee,
            'User': User,
            'Response': Response,
            'Match': Match}[key[0]]
    return clazz.objects.get(id=int(key[1]))

def send_mail(to, subject, body, bcc=False):
    if not settings.DEBUG:
        if not bcc:
            email = EmailMessage(subject, body, settings.EMAIL_FROM, [to,], [],
                    headers={'Reply-To':settings.LCS_EMAIL})
        else:
            email = EmailMessage(subject, body, settings.EMAIL_FROM, [to,],
                    [settings.LCS_EMAIL,],
                    headers={'Reply-To':settings.LCS_EMAIL})
        email.send(True)

