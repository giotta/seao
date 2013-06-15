# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Avis.slug'
        db.alter_column(u'api_avis', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True))

        # Changing field 'Soumission.slug'
        db.alter_column(u'api_soumission', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Avis.slug'
        raise RuntimeError("Cannot reverse this migration. 'Avis.slug' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Soumission.slug'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.slug' and its values cannot be restored.")

    models = {
        u'api.avis': {
            'Meta': {'object_name': 'Avis'},
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'date_adjudication': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date_publication': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date_saisie_adjudication': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'disposition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Disposition']"}),
            'municipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Nature']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'numero_seao': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'orgamisme': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Pays']"}),
            'precision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Province']"}),
            'regions_livraison': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Region']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Type']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'api.disposition': {
            'Meta': {'object_name': 'Disposition'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.nature': {
            'Meta': {'object_name': 'Nature'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.pays': {
            'Meta': {'object_name': 'Pays'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.province': {
            'Meta': {'object_name': 'Province'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.region': {
            'Meta': {'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.soumission': {
            'Meta': {'object_name': 'Soumission'},
            'adjudicataire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admissible': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'appel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'to': u"orm['api.Avis']"}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'conforme': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant_contrat': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis_unite': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'blank': 'True', 'to': u"orm['api.UniteMontant']"}),
            'nom_organisation': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'blank': 'True', 'to': u"orm['api.Pays']"}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'blank': 'True', 'to': u"orm['api.Province']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'api.type': {
            'Meta': {'object_name': 'Type'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.unitemontant': {
            'Meta': {'object_name': 'UniteMontant'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.unspsc': {
            'Meta': {'object_name': 'UNSPSC'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']