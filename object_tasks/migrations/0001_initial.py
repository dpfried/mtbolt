# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ObjectDescriptionTask'
        db.create_table('object_tasks_objectdescriptiontask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('completion_code', self.gf('django.db.models.fields.CharField')(default='06d9e2c8145b4ca58f3e2a0131e9c363', unique=True, max_length=32)),
            ('approved', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('object_tasks', ['ObjectDescriptionTask'])

        # Adding model 'EntityBinding'
        db.create_table('object_tasks_entitybinding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_bindings', to=orm['object_tasks.ObjectDescriptionTask'])),
            ('description', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entity_bindings', to=orm['tasks.DescriptionQuestion'])),
            ('binding', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('object_tasks', ['EntityBinding'])


    def backwards(self, orm):
        # Deleting model 'ObjectDescriptionTask'
        db.delete_table('object_tasks_objectdescriptiontask')

        # Deleting model 'EntityBinding'
        db.delete_table('object_tasks_entitybinding')


    models = {
        'object_tasks.entitybinding': {
            'Meta': {'object_name': 'EntityBinding'},
            'binding': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_bindings'", 'to': "orm['tasks.DescriptionQuestion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_bindings'", 'to': "orm['object_tasks.ObjectDescriptionTask']"})
        },
        'object_tasks.objectdescriptiontask': {
            'Meta': {'object_name': 'ObjectDescriptionTask'},
            'approved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'completion_code': ('django.db.models.fields.CharField', [], {'default': "'3190c44056214c58b761e7991424e747'", 'unique': 'True', 'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'scenes.entity': {
            'Meta': {'object_name': 'Entity'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entities'", 'to': "orm['scenes.Scene']"})
        },
        'scenes.scene': {
            'Meta': {'object_name': 'Scene'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'tasks.descriptionquestion': {
            'Meta': {'object_name': 'DescriptionQuestion'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'descriptions'", 'to': "orm['scenes.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenes.Scene']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['tasks.DescriptionTask']"}),
            'use_in_object_tasks': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'tasks.descriptiontask': {
            'Meta': {'object_name': 'DescriptionTask'},
            'approved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'completion_code': ('django.db.models.fields.CharField', [], {'default': "'e279d79813964ffbacc6e88977a411d4'", 'unique': 'True', 'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['object_tasks']