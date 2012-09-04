# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'AppSetting', fields ['name']
        db.create_unique('account_appsetting', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AppSetting', fields ['name']
        db.delete_unique('account_appsetting', ['name'])


    models = {
        'account.appsetting': {
            'Meta': {'object_name': 'AppSetting'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['account']
