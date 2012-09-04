# encoding: utf-8
import datetime
from account import app_settings
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.AppSetting.objects.create(name=app_settings.TUTOR_REG_EMAIL,
                description="Send email to tutors after they have successfully"\
                "registered", value=True)
        orm.AppSetting.objects.create(name=app_settings.TUTEE_REG_EMAIL,
                description="Send email to tutees after they have successfully"\
                "registered", value=True)


    def backwards(self, orm):
        orm.AppSetting.objects.get(name=app_settings.TUTOR_REG_EMAIL).delete()
        orm.AppSetting.objects.get(name=app_settings.TUTEE_REG_EMAIL).delete()


    models = {
        'account.appsetting': {
            'Meta': {'object_name': 'AppSetting'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['account']
