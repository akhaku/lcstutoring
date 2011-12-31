# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tutee'
        db.create_table('tutees_tutee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent_last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('child_first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('child_last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('home_phone_number', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('cell_phone_number', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('grade', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('subjects', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('tutees', ['Tutee'])


    def backwards(self, orm):
        
        # Deleting model 'Tutee'
        db.delete_table('tutees_tutee')


    models = {
        'tutees.tutee': {
            'Meta': {'object_name': 'Tutee'},
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
