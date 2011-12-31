# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tutor.active'
        db.add_column('tutors_tutor', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Tutor.active'
        db.delete_column('tutors_tutor', 'active')


    models = {
        'tutors.tutor': {
            'Meta': {'object_name': 'Tutor'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subjects': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tutoring_preference_from': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'tutoring_preference_to': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['tutors']
