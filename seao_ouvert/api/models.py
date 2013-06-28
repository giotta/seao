# coding: utf-8

from django.db import models


class ChoiceValue(models.Model):
    code = models.CharField(
        max_length=3,
        unique=True,
        )
    name = models.CharField(max_length=512)
    class Meta:
        abstract = True


class Province(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)


class Type(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)


class Nature(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)


class Region(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = u"Région"
        verbose_name_plural = u"Régions"


class DispositionNonMunicipale(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)


class DispositionMunicipale(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)


class Pays(ChoiceValue):
    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = u"Pays"
        verbose_name_plural = u"Pays"


class UniteMontant(ChoiceValue):

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = u"Unité de montant"
        verbose_name_plural = u"Unités de montant"


class UNSPSC(ChoiceValue):

    def __unicode__(self):
        return "%s" % (self.name,)

    class Meta:
        verbose_name = u"UNSPSC"
        verbose_name_plural = u"UNSPSC"


class Avis(models.Model):
    titre = models.CharField(
        max_length=255,
        )
    numero_seao = models.IntegerField(
        primary_key=True,
        )
    numero = models.CharField(
        max_length=25,
        )
    organisme = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    municipal = models.BooleanField()

    adresse1 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    adresse2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    ville = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )

    province = models.ForeignKey(
        Province,
        related_name='avis',
        blank=True,
        null=True,
        )
    pays = models.ForeignKey(
        Pays,
        related_name='avis',
        blank=True,
        null=True,
        )
    code_postal = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        )
    type = models.ForeignKey(
        Type,
        related_name='avis',
        blank=True,
        null=True,
        )
    nature = models.ForeignKey(
        Nature,
        related_name='avis',
        blank=True,
        null=True,
        )
    date_publication = models.DateTimeField(
        blank=True,
        null=True,
        )
    date_fermeture = models.DateTimeField(
        blank=True,
        null=True,
        )
    date_saisie_adjudication = models.DateTimeField(
        blank=True,
        null=True,
        )
    date_adjudication = models.DateField(
        blank=True,
        null=True,
        )
    regions_livraison = models.ManyToManyField(
        Region,
        related_name='avis',
        blank=True,
        null=True,
        )
    disposition_non_municipale = models.ForeignKey(
        DispositionNonMunicipale,
        related_name='avis',
        blank=True,
        null=True,
        )
    disposition_municipale = models.ForeignKey(
        DispositionMunicipale,
        related_name='avis',
        blank=True,
        null=True,
        )
    precision = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )

    def __unicode__(self):
        return "%s (%d)" % (self.titre, self.numero_seao)

    class Meta:
        verbose_name = u"Avis"
        verbose_name_plural = u"Avis"


class Soumission(models.Model):

    nom_organisation = models.CharField(
        max_length=255,
        )
    adresse1 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    adresse2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    ville = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        )
    province = models.ForeignKey(
        Province,
        related_name='soumissions',
        blank=True,
        null=True,
        )
    pays = models.ForeignKey(
        Pays,
        related_name='soumissions',
        blank=True,
        null=True,
        )
    code_postal = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        )
    admissible = models.NullBooleanField()
    conforme = models.NullBooleanField()
    adjudicataire = models.BooleanField()
    montant_soumis = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
        )
    montant_soumis_unite = models.ForeignKey(
        UniteMontant,
        blank=True,
        null=True,
        related_name='soumissions',
        )
    montant_contrat = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
        )

    appel = models.ForeignKey(
        Avis,
        related_name='soumissions',
        )

    def __unicode__(self):
        return "%s" % (self.nom_organisation,)
