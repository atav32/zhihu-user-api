# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZhihuUser'
        db.create_table(u'zhihuUser_zhihuuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=256, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('answers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('questions', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('edits', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('following', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('followers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('essays', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bookmarks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'zhihuUser', ['ZhihuUser'])

        # Adding model 'Question'
        db.create_table(u'zhihuUser_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('asker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zhihuUser.ZhihuUser'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('watchers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answers', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'zhihuUser', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'zhihuUser_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zhihuUser.Question'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('answerer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zhihuUser.ZhihuUser'])),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comments', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'zhihuUser', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'ZhihuUser'
        db.delete_table(u'zhihuUser_zhihuuser')

        # Deleting model 'Question'
        db.delete_table(u'zhihuUser_question')

        # Deleting model 'Answer'
        db.delete_table(u'zhihuUser_answer')


    models = {
        u'zhihuUser.answer': {
            'Meta': {'object_name': 'Answer'},
            'answerer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zhihuUser.ZhihuUser']"}),
            'comments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zhihuUser.Question']"}),
            'token': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'})
        },
        u'zhihuUser.question': {
            'Meta': {'object_name': 'Question'},
            'answers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'asker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zhihuUser.ZhihuUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'token': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'watchers': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'zhihuUser.zhihuuser': {
            'Meta': {'object_name': 'ZhihuUser'},
            'answers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bookmarks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'edits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'essays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'followers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'following': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'questions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['zhihuUser']