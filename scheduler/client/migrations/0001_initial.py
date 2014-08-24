# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'client_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('regularity', self.gf('django.db.models.fields.IntegerField')()),
            ('dayofweek', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('duration', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Notes'], null=True, blank=True)),
        ))
        db.send_create_signal(u'client', ['Client'])

        # Adding model 'Gap'
        db.create_table(u'client_gap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'client', ['Gap'])

        # Adding model 'Notes'
        db.create_table(u'client_notes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'client', ['Notes'])

        # Adding model 'Day'
        db.create_table(u'client_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(unique=True)),
            ('dayofweek', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('unfilled', self.gf('django.db.models.fields.SmallIntegerField')(default=8)),
        ))
        db.send_create_signal(u'client', ['Day'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'client_client')

        # Deleting model 'Gap'
        db.delete_table(u'client_gap')

        # Deleting model 'Notes'
        db.delete_table(u'client_notes')

        # Deleting model 'Day'
        db.delete_table(u'client_day')


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
        u'client.gap': {
            'Meta': {'object_name': 'Gap'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        u'client.notes': {
            'Meta': {'object_name': 'Notes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['client']