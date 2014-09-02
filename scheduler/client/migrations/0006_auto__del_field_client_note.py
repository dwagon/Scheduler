# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Client.note'
        db.delete_column(u'client_client', 'note_id')


    def backwards(self, orm):
        # Adding field 'Client.note'
        db.add_column(u'client_client', 'note',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['note.Note'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'dayofweek': ('django.db.models.fields.SmallIntegerField', [], {}),
            'duration': ('django.db.models.fields.SmallIntegerField', [], {}),
            'enddate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'flexible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'regularity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'})
        }
    }

    complete_apps = ['client']