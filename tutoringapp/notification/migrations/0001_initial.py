# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Notification'
        db.create_table('notification_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('notification', ['Notification'])


    def backwards(self, orm):
        
        # Deleting model 'Notification'
        db.delete_table('notification_notification')


    models = {
        'notification.notification': {
            'Meta': {'object_name': 'Notification'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['notification']
