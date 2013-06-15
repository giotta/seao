# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Disposition'
        db.delete_table(u'api_disposition')

        # Adding model 'DispositionMunicipale'
        db.create_table(u'api_dispositionmunicipale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['DispositionMunicipale'])

        # Adding model 'DispositionNonMunicipale'
        db.create_table(u'api_dispositionnonmunicipale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['DispositionNonMunicipale'])

        # Deleting field 'Avis.disposition'
        db.delete_column(u'api_avis', 'disposition_id')

        # Adding field 'Avis.disposition_non_municipale'
        db.add_column(u'api_avis', 'disposition_non_municipale',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='avis', null=True, to=orm['api.DispositionNonMunicipale']),
                      keep_default=False)

        # Adding field 'Avis.disposition_municipale'
        db.add_column(u'api_avis', 'disposition_municipale',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='avis', null=True, to=orm['api.DispositionMunicipale']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Disposition'
        db.create_table(u'api_disposition', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Disposition'])

        # Deleting model 'DispositionMunicipale'
        db.delete_table(u'api_dispositionmunicipale')

        # Deleting model 'DispositionNonMunicipale'
        db.delete_table(u'api_dispositionnonmunicipale')


        # User chose to not deal with backwards NULL issues for 'Avis.disposition'
        raise RuntimeError("Cannot reverse this migration. 'Avis.disposition' and its values cannot be restored.")
        # Deleting field 'Avis.disposition_non_municipale'
        db.delete_column(u'api_avis', 'disposition_non_municipale_id')

        # Deleting field 'Avis.disposition_municipale'
        db.delete_column(u'api_avis', 'disposition_municipale_id')


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
            'disposition_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionMunicipale']"}),
            'disposition_non_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionNonMunicipale']"}),
            'municipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Nature']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'numero_seao': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'orgamisme': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Pays']"}),
            'precision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Province']"}),
            'regions_livraison': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Region']"}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'avis'", 'blank': 'True', 'to': u"orm['api.Type']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'api.dispositionmunicipale': {
            'Meta': {'object_name': 'DispositionMunicipale'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.dispositionnonmunicipale': {
            'Meta': {'object_name': 'DispositionNonMunicipale'},
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