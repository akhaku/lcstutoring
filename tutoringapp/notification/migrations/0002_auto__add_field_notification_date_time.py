# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Notification.date_time'
        db.add_column('notification_notification', 'date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 9, 3, 3, 9, 37, 33830), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Notification.date_time'
        db.delete_column('notification_notification', 'date_time')


    models = {
        'notification.notification': {
            'Meta': {'object_name': 'Notification'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['notification']
