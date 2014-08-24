# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visit'
        db.create_table(u'visit_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Client'])),
            ('good', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Day'])),
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Notes'], null=True, blank=True)),
        ))
        db.send_create_signal(u'visit', ['Visit'])

        # Adding unique constraint on 'Visit', fields ['client', 'date']
        db.create_unique(u'visit_visit', ['client_id', 'date_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Visit', fields ['client', 'date']
        db.delete_unique(u'visit_visit', ['client_id', 'date_id'])

        # Deleting model 'Visit'
        db.delete_table(u'visit_visit')


    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'dayofweek': ('django.db.models.fields.SmallIntegerField', [], {}),
            'duration': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Notes']", 'null': 'True', 'blank': 'True'}),
            'regularity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'client.day': {
            'Meta': {'object_name': 'Day'},
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'dayofweek': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unfilled': ('django.db.models.fields.SmallIntegerField', [], {'default': '8'})
        },
        u'client.notes': {
            'Meta': {'object_name': 'Notes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'visit.visit': {
            'Meta': {'unique_together': "(('client', 'date'),)", 'object_name': 'Visit'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Client']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Day']"}),
            'good': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Notes']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['visit']