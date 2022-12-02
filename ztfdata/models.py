### data/models.py ###
from uuid import uuid4
from django.db import models
from django.conf import settings
# Create your models here.


class PandasData(models.Model):
    index = models.IntegerField(primary_key=True)
    field = models.IntegerField()
    ccdid = models.IntegerField()
    qid = models.IntegerField()
    filter = models.CharField(max_length=5, null=True)
    pid = models.BigIntegerField()
    infobitssci = models.IntegerField()
    sciinpseeing = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    scibckgnd = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    scisigpix = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    zpmaginpsci = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    zpmaginpsciunc = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    zpmaginpscirms = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    clrcoeff = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    clrcoeffunc = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True)
    ncalmatches = models.IntegerField()
    exptime = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    adpctdif1 =  models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    adpctdif2 = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    diffmaglim = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    zpdiff = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    programid = models.IntegerField()
    jd = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    rfid = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimflux = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimfluxunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimsnr = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimchisq = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimfluxap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimfluxuncap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    forcediffimsnrap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    aperturecorr = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    dnearestrefsrc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    nearestrefmag = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    nearestrefmagunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    nearestrefmagunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    nearestrefchi = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    nearestrefsharp = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    refjdstart = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    refjdend = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    procstatus = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.index


    # class Meta:
    #     ordering = ['index']