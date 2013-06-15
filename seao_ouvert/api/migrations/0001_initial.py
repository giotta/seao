# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Province'
        db.create_table(u'api_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Province'])

        # Adding model 'Type'
        db.create_table(u'api_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Type'])

        # Adding model 'Nature'
        db.create_table(u'api_nature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Nature'])

        # Adding model 'Region'
        db.create_table(u'api_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Region'])

        # Adding model 'Disposition'
        db.create_table(u'api_disposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Disposition'])

        # Adding model 'Pays'
        db.create_table(u'api_pays', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Pays'])

        # Adding model 'UniteMontant'
        db.create_table(u'api_unitemontant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['UniteMontant'])

        # Adding model 'UNSPSC'
        db.create_table(u'api_unspsc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['UNSPSC'])

        # Adding model 'Avis'
        db.create_table(u'api_avis', (
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('numero_seao', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('orgamisme', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('municipal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(related_name='avis', blank=True, to=orm['api.Province'])),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='avis', blank=True, to=orm['api.Pays'])),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=7, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='avis', blank=True, to=orm['api.Type'])),
            ('nature', self.gf('django.db.models.fields.related.ForeignKey')(related_name='avis', blank=True, to=orm['api.Nature'])),
            ('date_publication', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('date_fermeture', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('date_saisie_adjudication', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('date_adjudication', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('disposition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='avis', blank=True, to=orm['api.Disposition'])),
            ('precision', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal(u'api', ['Avis'])

        # Adding M2M table for field regions_livraison on 'Avis'
        m2m_table_name = db.shorten_name(u'api_avis_regions_livraison')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('avis', models.ForeignKey(orm[u'api.avis'], null=False)),
            ('region', models.ForeignKey(orm[u'api.region'], null=False))
        ))
        db.create_unique(m2m_table_name, ['avis_id', 'region_id'])

        # Adding model 'Soumission'
        db.create_table(u'api_soumission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_organisation', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(related_name='soumissions', blank=True, to=orm['api.Province'])),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='soumissions', blank=True, to=orm['api.Pays'])),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=7, blank=True)),
            ('admissible', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('conforme', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('adjudicataire', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('montant_soumis', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2, blank=True)),
            ('montant_soumis_unite', self.gf('django.db.models.fields.related.ForeignKey')(related_name='soumissions', blank=True, to=orm['api.UniteMontant'])),
            ('montant_contrat', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2, blank=True)),
            ('appel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='soumissions', to=orm['api.Avis'])),
        ))
        db.send_create_signal(u'api', ['Soumission'])


    def backwards(self, orm):
        # Deleting model 'Province'
        db.delete_table(u'api_province')

        # Deleting model 'Type'
        db.delete_table(u'api_type')

        # Deleting model 'Nature'
        db.delete_table(u'api_nature')

        # Deleting model 'Region'
        db.delete_table(u'api_region')

        # Deleting model 'Disposition'
        db.delete_table(u'api_disposition')

        # Deleting model 'Pays'
        db.delete_table(u'api_pays')

        # Deleting model 'UniteMontant'
        db.delete_table(u'api_unitemontant')

        # Deleting model 'UNSPSC'
        db.delete_table(u'api_unspsc')

        # Deleting model 'Avis'
        db.delete_table(u'api_avis')

        # Removing M2M table for field regions_livraison on 'Avis'
        db.delete_table(db.shorten_name(u'api_avis_regions_livraison'))

        # Deleting model 'Soumission'
        db.delete_table(u'api_soumission')


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