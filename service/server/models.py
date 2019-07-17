# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Stage(models.Model):
    attributename = models.CharField(primary_key=True, max_length=45)
    stage = models.CharField(max_length=45, blank=True, null=True)
    stageindex = models.CharField(db_column='stageIndex', max_length=45, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=45, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stage'


class UpdatedAki(models.Model):
    inpatient_id = models.TextField(db_column='INPATIENT_ID', blank=True, null=True)  # Field name made lowercase.
    procedure_date = models.TextField(db_column='Procedure_Date', blank=True, null=True)  # Field name made lowercase.
    in_hos_datetime = models.BigIntegerField(db_column='IN_HOS_DATETIME', blank=True, null=True)  # Field name made lowercase.
    out_hos_datetime = models.BigIntegerField(db_column='OUT_HOS_DATETIME', blank=True, null=True)  # Field name made lowercase.
    aki_stage = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(blank=True, null=True)
    anemia = models.IntegerField(blank=True, null=True)
    diabetes = models.IntegerField(blank=True, null=True)
    cardiac_failure = models.TextField(blank=True, null=True)
    iabp = models.IntegerField(db_column='IABP', blank=True, null=True)  # Field name made lowercase.
    hypotension = models.IntegerField(blank=True, null=True)
    contrast_dosage_ml_field = models.IntegerField(db_column='contrast dosage (mL)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gfr = models.FloatField(blank=True, null=True)
    myocardial_infarction = models.IntegerField(db_column='myocardial infarction', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hypercholesterolemia = models.IntegerField(db_column='Hypercholesterolemia', blank=True, null=True)  # Field name made lowercase.
    hdl_c = models.FloatField(db_column='HDL-C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urgent_pci = models.IntegerField(db_column='urgent_PCI', blank=True, null=True)  # Field name made lowercase.
    pre_crea = models.FloatField(db_column='Pre_Crea', blank=True, null=True)  # Field name made lowercase.
    hp = models.TextField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'updated_aki'
