# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Notes'
        db.delete_table(u'client_notes')

        # Deleting model 'Gap'
        db.delete_table(u'client_gap')


        # Changing field 'Client.note'
        db.alter_column(u'client_client', 'note_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['note.Note'], null=True))

    def backwards(self, orm):
        # Adding model 'Notes'
        db.create_table(u'client_notes', (
            ('note', self.gf('django.db.models.fields.CharField')(max_length=250)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'client', ['Notes'])

        # Adding model 'Gap'
        db.create_table(u'client_gap', (
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'client', ['Gap'])


        # Changing field 'Client.note'
        db.alter_column(u'client_client', 'note_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client.Notes'], null=True))

    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'dayofweek': ('django.db.models.fields.SmallIntegerField', [], {}),
            'duration': ('django.db.models.fields.SmallIntegerField', [], {}),
            'flexible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note.Note']", 'null': 'True', 'blank': 'True'}),
            'regularity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'note.note': {
            'Meta': {'object_name': 'Note'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['client']