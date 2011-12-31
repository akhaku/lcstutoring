# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tutor.phone_number'
        db.add_column('tutors_tutor', 'phone_number', self.gf('django.db.models.fields.CharField')(default="987-654-3210", max_length=15), keep_default=False)

        # Adding field 'Tutor.grad_year'
        db.add_column('tutors_tutor', 'grad_year', self.gf('django.db.models.fields.IntegerField')(default=2012, max_length=4), keep_default=False)

        # Adding field 'Tutor.tutoring_preference_from'
        db.add_column('tutors_tutor', 'tutoring_preference_from', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2), keep_default=False)

        # Adding field 'Tutor.tutoring_preference_to'
        db.add_column('tutors_tutor', 'tutoring_preference_to', self.gf('django.db.models.fields.IntegerField')(default=9, max_length=2), keep_default=False)

        # Adding field 'Tutor.subjects'
        db.add_column('tutors_tutor', 'subjects', self.gf('django.db.models.fields.CharField')(default='All', max_length=50), keep_default=False)

        # Adding field 'Tutor.note'
        db.add_column('tutors_tutor', 'note', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Tutor.phone_number'
        db.delete_column('tutors_tutor', 'phone_number')

        # Deleting field 'Tutor.grad_year'
        db.delete_column('tutors_tutor', 'grad_year')

        # Deleting field 'Tutor.tutoring_preference_from'
        db.delete_column('tutors_tutor', 'tutoring_preference_from')

        # Deleting field 'Tutor.tutoring_preference_to'
        db.delete_column('tutors_tutor', 'tutoring_preference_to')

        # Deleting field 'Tutor.subjects'
        db.delete_column('tutors_tutor', 'subjects')

        # Deleting field 'Tutor.note'
        db.delete_column('tutors_tutor', 'note')


    models = {
        'tutors.tutor': {
            'Meta': {'object_name': 'Tutor'},
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
