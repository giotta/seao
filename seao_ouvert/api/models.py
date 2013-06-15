from django.db import models


class ChoiceValue(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    class Meta:
        abstract = True


class Province(ChoiceValue):
    pass


class Type(ChoiceValue):
    pass


class Nature(ChoiceValue):
    pass


class Region(ChoiceValue):
    pass


class Disposition(ChoiceValue):
    pass


class Pays(ChoiceValue):
    pass


class UniteMontant(ChoiceValue):
    pass


class UNSPSC(ChoiceValue):
    pass


class Avis(models.Model):
    titre = models.CharField(
        max_length=150,
        )
    numero_seao = models.IntegerField(
        primary_key=True,
        )
    numero = models.CharField(
        max_length=25,
        )
    orgamisme = models.CharField(
        max_length=150,
        blank=True,
        )
    municipal = models.BooleanField()
    adresse1 = models.CharField(
        max_length=60,
        blank=True,
        )
    adresse2 = models.CharField(
        max_length=60,
        blank=True,
        )
    ville = models.CharField(
        max_length=40,
        blank=True,
        )
    province = models.ForeignKey(
        Province,
        related_name='avis',
        blank=True,
        )
    pays = models.ForeignKey(
        Pays,
        related_name='avis',
        blank=True,
        )
    code_postal = models.CharField(
        max_length=7,
        blank=True,
        )
    type = models.ForeignKey(
        Type,
        related_name='avis',
        blank=True,
        )
    nature = models.ForeignKey(
        Nature,
        related_name='avis',
        blank=True,
        )
    date_publication = models.DateTimeField(
        blank=True,
        )
    date_fermeture = models.DateTimeField(
        blank=True,
        )
    date_saisie_adjudication = models.DateTimeField(
        blank=True,
        )
    date_adjudication = models.DateField(
        blank=True,
        )
    regions_livraison = models.ManyToManyField(
        Region,
        related_name='avis',
        blank=True,
        )
    disposition = models.ForeignKey(
        Disposition,
        related_name='avis',
        blank=True,
        )
    precision = models.CharField(
        max_length=150,
        blank=True,
        )


class Soumission(models.Model):
    nom_organisation = models.CharField(
        max_length=80,
        )
    adresse1 = models.CharField(
        max_length=60,
        blank=True,
        )
    adresse2 = models.CharField(
        max_length=60,
        blank=True,
        )
    ville = models.CharField(
        max_length=40,
        blank=True,
        )
    province = models.ForeignKey(
        Province,
        related_name='soumissions',
        blank=True,
        )
    pays = models.ForeignKey(
        Pays,
        related_name='soumissions',
        blank=True,
        )
    code_postal = models.CharField(
        max_length=7,
        blank=True,
        )
    admissible = models.NullBooleanField()
    conforme = models.NullBooleanField()
    adjudicataire = models.BooleanField()
    montant_soumis = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        )
    montant_soumis_unite = models.ForeignKey(
        UniteMontant,
        blank=True,
        related_name='soumissions',
        )
    montant_contrat = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        )

    appel = models.ForeignKey(
        Avis,
        related_name='soumissions',
        )
