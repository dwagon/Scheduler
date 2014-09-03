# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Visit.note'
        db.delete_column(u'visit_visit', 'note_id')


    def backwards(self, orm):
        # Adding field 'Visit.note'
        db.add_column(u'visit_visit', 'note',
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
            'note': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'regularity': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'})
        },
        u'visit.visit': {
            'Meta': {'unique_together': "(('client', 'date'),)", 'object_name': 'Visit'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['client.Client']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'good': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['visit']