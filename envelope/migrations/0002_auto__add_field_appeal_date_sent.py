# -*- coding: utf-8 -*-
from datetime import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Appeal.date_sent'
        db.add_column(u'envelope_appeal', 'date_sent',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.now(), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Appeal.date_sent'
        db.delete_column(u'envelope_appeal', 'date_sent')


    models = {
        u'envelope.appeal': {
            'Meta': {'object_name': 'Appeal'},
            'date_sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['envelope']