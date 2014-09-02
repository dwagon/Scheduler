# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.startdate'
        db.add_column(u'client_client', 'startdate',
                      self.gf('django.db.models.fields.DateField')(default=None, null=True),
                      keep_default=False)

        # Adding field 'Client.enddate'
        db.add_column(u'client_client', 'enddate',
                      self.gf('django.db.models.fields.DateField')(default=None, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.startdate'
        db.delete_column(u'client_client', 'startdate')

        # Deleting field 'Client.enddate'
        db.delete_column(u'client_client', 'enddate')


    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'dayofweek': ('django.db.models.fields.SmallIntegerField', [], {}),
            'duration': ('django.db.models.fields.SmallIntegerField', [], {}),
            'enddate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'flexible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['note.Note']", 'null': 'True', 'blank': 'True'}),
            'regularity': ('django.db.models.fields.IntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'})
        },
        u'note.note': {
            'Meta': {'object_name': 'Note'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['client']