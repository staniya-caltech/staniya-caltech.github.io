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
    filter = models.CharField(max_length=5, null=True, blank=True)
    pid = models.BigIntegerField()
    infobitssci = models.IntegerField()
    sciinpseeing = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    scibckgnd = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    scisigpix = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    zpmaginpsci = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    zpmaginpsciunc = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    zpmaginpscirms = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    clrcoeff = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    clrcoeffunc = models.DecimalField(
        max_digits=100,   decimal_places=15, null=True, blank=True)
    ncalmatches = models.IntegerField()
    exptime = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    adpctdif1 =  models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    adpctdif2 = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    diffmaglim = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    zpdiff = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    programid = models.IntegerField()
    jd = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    rfid = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimflux = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimfluxunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimsnr = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimchisq = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimfluxap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimfluxuncap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    forcediffimsnrap = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    aperturecorr = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    dnearestrefsrc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    nearestrefmag = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    nearestrefmagunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    nearestrefmagunc = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    nearestrefchi = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    nearestrefsharp = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    refjdstart = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    refjdend = models.DecimalField(
        max_digits=100, decimal_places=15, null=True, blank=True)
    procstatus = models.IntegerField()

    def __str__(self):
        return self.index


    class Meta:
        ordering = ['index']