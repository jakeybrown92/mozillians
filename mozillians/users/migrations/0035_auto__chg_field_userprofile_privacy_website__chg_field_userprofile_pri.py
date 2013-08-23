# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.privacy_website'
        db.alter_column('profile', 'privacy_website', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_region'
        db.alter_column('profile', 'privacy_region', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_full_name'
        db.alter_column('profile', 'privacy_full_name', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.vouched_by'
        db.alter_column('profile', 'vouched_by_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.SET_NULL, to=orm['users.UserProfile'], null=True))

        # Changing field 'UserProfile.privacy_email'
        db.alter_column('profile', 'privacy_email', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_groups'
        db.alter_column('profile', 'privacy_groups', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_ircname'
        db.alter_column('profile', 'privacy_ircname', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_date_mozillian'
        db.alter_column('profile', 'privacy_date_mozillian', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_city'
        db.alter_column('profile', 'privacy_city', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_skills'
        db.alter_column('profile', 'privacy_skills', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_photo'
        db.alter_column('profile', 'privacy_photo', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_bio'
        db.alter_column('profile', 'privacy_bio', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_timezone'
        db.alter_column('profile', 'privacy_timezone', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_vouched_by'
        db.alter_column('profile', 'privacy_vouched_by', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_country'
        db.alter_column('profile', 'privacy_country', self.gf('mozillians.users.models.PrivacyField')())

        # Changing field 'UserProfile.privacy_languages'
        db.alter_column('profile', 'privacy_languages', self.gf('mozillians.users.models.PrivacyField')())

    def backwards(self, orm):

        # Changing field 'UserProfile.privacy_website'
        db.alter_column('profile', 'privacy_website', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_region'
        db.alter_column('profile', 'privacy_region', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_full_name'
        db.alter_column('profile', 'privacy_full_name', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.vouched_by'
        db.alter_column('profile', 'vouched_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['users.UserProfile']))

        # Changing field 'UserProfile.privacy_email'
        db.alter_column('profile', 'privacy_email', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_groups'
        db.alter_column('profile', 'privacy_groups', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_ircname'
        db.alter_column('profile', 'privacy_ircname', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_date_mozillian'
        db.alter_column('profile', 'privacy_date_mozillian', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_city'
        db.alter_column('profile', 'privacy_city', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_skills'
        db.alter_column('profile', 'privacy_skills', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_photo'
        db.alter_column('profile', 'privacy_photo', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_bio'
        db.alter_column('profile', 'privacy_bio', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_timezone'
        db.alter_column('profile', 'privacy_timezone', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_vouched_by'
        db.alter_column('profile', 'privacy_vouched_by', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_country'
        db.alter_column('profile', 'privacy_country', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'UserProfile.privacy_languages'
        db.alter_column('profile', 'privacy_languages', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'groups.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            'always_auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irc_channel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'steward': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.UserProfile']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'system': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'wiki': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'groups.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            'always_auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        'groups.skill': {
            'Meta': {'ordering': "['name']", 'object_name': 'Skill'},
            'always_auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        'users.usernameblacklist': {
            'Meta': {'ordering': "['value']", 'object_name': 'UsernameBlacklist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_regex': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'users.userprofile': {
            'Meta': {'ordering': "['full_name']", 'object_name': 'UserProfile', 'db_table': "'profile'"},
            'allows_community_sites': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allows_mozilla_sites': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'basket_token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'date_mozillian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_vouched': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': "orm['groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ircname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63', 'blank': 'True'}),
            'is_vouched': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': "orm['groups.Language']"}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'privacy_bio': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_city': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_country': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_date_mozillian': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_email': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_full_name': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_groups': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_ircname': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_languages': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_photo': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_region': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_skills': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_timezone': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_vouched_by': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'privacy_website': ('mozillians.users.models.PrivacyField', [], {'default': '3'}),
            'region': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': "orm['groups.Skill']"}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'vouched_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vouchees'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['users.UserProfile']", 'blank': 'True', 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['users']