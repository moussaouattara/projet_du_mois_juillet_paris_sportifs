# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Joueur'
        db.create_table(u'football_joueur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'football', ['Joueur'])

        # Adding model 'Equipe'
        db.create_table(u'football_equipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('poule', self.gf('django.db.models.fields.CharField')(default=u'A', max_length=1)),
            ('drapeau', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'football', ['Equipe'])

        # Adding model 'Match'
        db.create_table(u'football_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('niveau', self.gf('django.db.models.fields.CharField')(default=u'Match de poule', max_length=20)),
            ('equipe1', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'equipe1_content_type', to=orm['football.Equipe'])),
            ('equipe2', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'equipe2_content_type', to=orm['football.Equipe'])),
            ('equipe1_result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('equipe2_result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('traite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'football', ['Match'])

        # Adding model 'Pronostic'
        db.create_table(u'football_pronostic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('joueur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['football.Match'])),
            ('equipe1_result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('equipe2_result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'football', ['Pronostic'])

        # Adding unique constraint on 'Pronostic', fields ['joueur', 'match']
        db.create_unique(u'football_pronostic', ['joueur_id', 'match_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Pronostic', fields ['joueur', 'match']
        db.delete_unique(u'football_pronostic', ['joueur_id', 'match_id'])

        # Deleting model 'Joueur'
        db.delete_table(u'football_joueur')

        # Deleting model 'Equipe'
        db.delete_table(u'football_equipe')

        # Deleting model 'Match'
        db.delete_table(u'football_match')

        # Deleting model 'Pronostic'
        db.delete_table(u'football_pronostic')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'football.equipe': {
            'Meta': {'ordering': "[u'poule', u'nom']", 'object_name': 'Equipe'},
            'drapeau': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poule': ('django.db.models.fields.CharField', [], {'default': "u'A'", 'max_length': '1'})
        },
        u'football.joueur': {
            'Meta': {'object_name': 'Joueur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'football.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equipe1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipe1_content_type'", 'to': u"orm['football.Equipe']"}),
            'equipe1_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equipe2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'equipe2_content_type'", 'to': u"orm['football.Equipe']"}),
            'equipe2_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'niveau': ('django.db.models.fields.CharField', [], {'default': "u'Match de poule'", 'max_length': '20'}),
            'traite': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'football.pronostic': {
            'Meta': {'unique_together': "((u'joueur', u'match'),)", 'object_name': 'Pronostic'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equipe1_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'equipe2_result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joueur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Match']"})
        }
    }

    complete_apps = ['football']