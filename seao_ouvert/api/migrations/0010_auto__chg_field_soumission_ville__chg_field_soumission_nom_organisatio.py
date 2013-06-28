# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Soumission.ville'
        db.alter_column(u'api_soumission', 'ville', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Soumission.nom_organisation'
        db.alter_column(u'api_soumission', 'nom_organisation', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Soumission.adresse1'
        db.alter_column(u'api_soumission', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Soumission.adresse2'
        db.alter_column(u'api_soumission', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Avis.ville'
        db.alter_column(u'api_avis', 'ville', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Avis.precision'
        db.alter_column(u'api_avis', 'precision', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Avis.organisme'
        db.alter_column(u'api_avis', 'organisme', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Avis.titre'
        db.alter_column(u'api_avis', 'titre', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Avis.adresse1'
        db.alter_column(u'api_avis', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Avis.adresse2'
        db.alter_column(u'api_avis', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Soumission.ville'
        db.alter_column(u'api_soumission', 'ville', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Soumission.nom_organisation'
        db.alter_column(u'api_soumission', 'nom_organisation', self.gf('django.db.models.fields.CharField')(max_length=80))

        # Changing field 'Soumission.adresse1'
        db.alter_column(u'api_soumission', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Soumission.adresse2'
        db.alter_column(u'api_soumission', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Avis.ville'
        db.alter_column(u'api_avis', 'ville', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Avis.precision'
        db.alter_column(u'api_avis', 'precision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Avis.organisme'
        db.alter_column(u'api_avis', 'organisme', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Avis.titre'
        db.alter_column(u'api_avis', 'titre', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Avis.adresse1'
        db.alter_column(u'api_avis', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Avis.adresse2'
        db.alter_column(u'api_avis', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    models = {
        u'api.avis': {
            'Meta': {'object_name': 'Avis'},
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'date_adjudication': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_publication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_saisie_adjudication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'disposition_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionMunicipale']"}),
            'disposition_non_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionNonMunicipale']"}),
            'municipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Nature']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'numero_seao': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'organisme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Pays']"}),
            'precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Province']"}),
            'regions_livraison': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['api.Region']"}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Type']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'api.dispositionmunicipale': {
            'Meta': {'object_name': 'DispositionMunicipale'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.dispositionnonmunicipale': {
            'Meta': {'object_name': 'DispositionNonMunicipale'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.nature': {
            'Meta': {'object_name': 'Nature'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.pays': {
            'Meta': {'object_name': 'Pays'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.province': {
            'Meta': {'object_name': 'Province'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.region': {
            'Meta': {'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.soumission': {
            'Meta': {'object_name': 'Soumission'},
            'adjudicataire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admissible': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'appel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'to': u"orm['api.Avis']"}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'conforme': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant_contrat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis_unite': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.UniteMontant']"}),
            'nom_organisation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.Pays']"}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.Province']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'api.type': {
            'Meta': {'object_name': 'Type'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.unitemontant': {
            'Meta': {'object_name': 'UniteMontant'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.unspsc': {
            'Meta': {'object_name': 'UNSPSC'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['api']