# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tutee.active'
        db.add_column('tutees_tutee', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Tutee.active'
        db.delete_column('tutees_tutee', 'active')


    models = {
        'tutees.tutee': {
            'Meta': {'object_name': 'Tutee'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'cell_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'child_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'child_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'home_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parent_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subjects': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tutees']
