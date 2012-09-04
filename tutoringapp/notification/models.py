from time import strftime
from django.db import models
from tmsutil import send_mail
from account.models import AppSetting
from account import app_settings
from notification import actions, email_strings as emails
from tmsutil import model_to_key as m2k, key_to_model as k2m

class NotificationManager(models.Manager):
    """ Defines methods used by callers when events happen. The types of
        events are defined in actions.py. These methods are the only ones that
        should be called to create notifications/send emails etc
    """
    def register_tutee(self, ttee):
        Notification.objects.create(sender=m2k(ttee),
                action=actions.REGISTERED_TUTEE)
        if Appsetting.objects.get(name=app_settings.TUTEE_REG_EMAIL).value:
            send_mail(ttee.email_address, emails.TUTEE_REG_SUBJECT,
                    emails.TUTEE_REG_BODY, True)

    def register_tutor(self, ttor):
        Notification.objects.create(sender=m2k(ttor),
                action=actions.REGISTERED_TUTOR)
        if Appsetting.objects.get(name=app_settings.TUTOR_REG_EMAIL).value:
            send_mail(ttor.email_address, emails.TUTOR_REG_SUBJECT,
                    emails.TUTOR_REG_BODY, True)

    def edit_tutee(self, user, tutee):
        Notification.objects.create(sender=m2k(user), recipient=m2k(tutee),
                action=actions.EDITED_TUTEE)

    def delete_tutee(self, user, tutee):
        Notification.objects.create(sender=m2k(user), recipient=m2k(tutee),
                action=actions.DELETED_TUTEE)

    def edit_tutor(self, user, tutor):
        Notification.objects.create(sender=m2k(user), recipient=m2k(tutor),
                action=actions.EDITED_TUTOR)

    def delete_tutor(self, user, tutor):
        Notification.objects.create(sender=m2k(user), recipient=m2k(tutor),
                action=actions.DELETED_TUTOR)

    def create_response(self, user, response):
        Notification.objects.create(sender=m2k(user), recipient=m2k(response),
                action=actions.CREATED_RESPONSE)

    def edit_response(self, user, response):
        Notification.objects.create(sender=m2k(user), recipient=m2k(response),
                action=actions.EDITED_RESPONSE)

    def delete_response(self, user, response):
        Notification.objects.create(sender=m2k(user), recipient=m2k(response),
                action=actions.DELETED_RESPONSE)

    def create_match(self, user, match):
        Notification.objects.create(sender=m2k(user), recipient=m2k(match),
                action=actions.MATCHED)

    def edit_match(self, user, match):
        Notification.objects.create(sender=m2k(user), recipient=m2k(match),
                action=actions.EDITED_MATCH)

    def delete_match(self, user, match):
        Notification.objects.create(sender=m2k(user), recipient=m2k(match),
                action=actions.DELETED_MATCH)

    def create_user(self, user, new_user):
        Notification.objects.create(sender=m2k(user), recipient=m2k(new_user),
                action=actions.CREATED_RESPONSE)

class Notification(models.Model):
    """ The base class for a notification. Should never be instantiated by any
        caller except for NotificationManager
    """
    # Stored as model/id eg Tutor/3
    sender = models.CharField(max_length=50)

    # Stored as model/id eg Tutor/3
    recipient = models.CharField(max_length=50, null=True)

    date_time = models.DateTimeField(auto_now_add=True)

    action = models.CharField(max_length=50)
    objects = NotificationManager()

    def __unicode__(self):
        date_str = self.date_time.strftime("on %a %b %e at %I:%M%p")
        if self.action == actions.REGISTERED_TUTEE or \
                self.action == actions.REGISTERED_TUTOR:
            ret = "%s %s" % (k2m(self.sender), self.action)
        else:
            ret = "%s %s %s" % (k2m(self.sender), self.action,
                    k2m(self.recipient))
        return "%s %s" % (ret, date_str)
