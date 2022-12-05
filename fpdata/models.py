### data/models.py ###
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class ZTFFPSData(models.Model):
    """
    index = sequential counter
    field = ZTF Field identifier
    ccdid = CCD identifier (1..16)
    qid = Quadrant (CCD-amplifier) identifier (0..3)
    filter = Filter string: ZTF_g, ZTF_r, ZTF_i
    pid = processed image Operations DB identifier
    infobitssci = processing summary/QA bits for sci image
    sciinpseeing = Effective FWHM of sci image [pixels]
    scibckgnd = Background level in sci image [DN]
    scisigpix = Robust sigma per pixel in sci image [DN]
    zpmaginpsci = Photometric zeropoint for sci image [mag]
    zpmaginpsciunc = 1-sigma uncertainty in zpmaginpsci [mag]
    zpmaginpscirms = RMS (deviation from average) in difference between instrumental mags and PS1 calibrators [mag]
    clrcoeff = Linear color coefficient from calibration; for ZTF_g,r,i, PS1 color used is g-r, g-r, r-i respectively
    clrcoeffunc = 1-sigma uncertainty in clrcoeff
    ncalmatches = Number of PS1 calibrators used in initial calibration of sci image
    exptime = Integration time for sci image [sec]
    adpctdif1 = Full sci image astrometric RMS along R.A. with respect to Gaia1 [arcsec]
    adpctdif2 = Full sci image astrometric RMS along Dec. with respect to Gaia1 [arcsec]
    diffmaglim = Magnitude limit in difference image [mag]
    zpdiff = Photometric zeropoint for difference image [mag]
    programid = Program identifier [0=engineering; 1=public; 2=private; 3=Caltech time]
    jd = Julian Date at start of exposure [days]
    rfid = Rerence image Operations DB identifier
    forcediffimflux = Forced difference image PSF-fit flux [DN]
    forcediffimfluxunc = 1-sigma uncertainty in forcediffimflux [DN]
    forcediffimsnr = Signal-to-noise ratio for forcediffimflux measurement
    forcediffimchisq = Reduced chi-square in PSF-fit
    forcediffimfluxap = Forced difference image aperture flux using a fixed 9-pixel diameter aperture [DN]
    forcediffimfluxuncap = 1-sigma uncertainty in forcediffimfluxap [DN]
    forcediffimsnrap = Signal-to-noise ratio for forcediffimfluxap measurement
    aperturecorr = Aperture (curve-of-growth) correction factor that was applied to forcediffimfluxap measurement
    dnearestrefsrc = Distance to nearest ref image source if found within 5 arcsec [arcsec]
    nearestrefmag = Magnitude of nearest ref image source [mag]
    nearestrefmagunc = 1-sigma uncertainty in nearestrefmag [mag]
    nearestrefchi = Chi parameter for nearestrefmag measurement (ratio: RMS in PSF-fit residuals / expected RMS from priors)
    nearestrefsharp = Sharp parameter for nearestrefmag measurement (~0 => PSF like; >>0 => extended; <<0 => pixel spike or hard edge)
    refjdstart = JD of earliest sci image used for ref image [days]
    refjdend = JD of latest sci image used for ref image [days]
    procstatus = Per-epoch processing status codes (0 => no warnings); if non-zero, see accompanying log file and document link below
    """
    index = models.IntegerField(primary_key=True)
    field = models.IntegerField(null=True)
    ccdid = models.IntegerField(null=True)
    qid = models.IntegerField(null=True)
    filter = models.CharField(max_length=5, null=True)
    pid = models.BigIntegerField(null=True)
    infobitssci = models.IntegerField(null=True)
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
    ncalmatches = models.IntegerField(null=True)
    exptime = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    adpctdif1 = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    adpctdif2 = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    diffmaglim = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    zpdiff = models.DecimalField(
        max_digits=100, decimal_places=15, null=True)
    programid = models.IntegerField(null=True)
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


class MROZData(models.Model):
    """
    bjd = Mid-exposure barycentric julian date, corrected using reference image central RA and Dec [days]
    mag = Source magnitude using above intrumental magnitude to scale the difference image flux [mag]
    magerr = Uncertainty on source magnitude [mag]
    diffimflux = Forced difference image PSF flux [DN]
    diffimfluxunc = 1-sigma uncertainty on diffimflux [DN]
    flag = 0 (if diffimflux is not NaN), or 1 (if diffimflux in NaN)
    filterid = 1 for g-band, 2 for r-band, or 3 for i-band
    exptime = Exposure time of the image [s]
    pid = ZTF Program ID (1, 2, or 3)
    field = ZTF Field ID
    ccd = ZTF CCD ID (1-16)
    quad = ZTF Quadrant ID (1-4)
    status = Image status (0 = bad image, 1 = good image)
    infobits = Processing summary/QA bits for science image
    seeing = Effective FWHM of sci image [pixels]
    zpmagsci = Photometric zeropoint for science image [mag]
    zpmagsciunc = 1-sigma uncertainty on zpmagsci [mag]
    zpmagscirms = RMS deviation in difference between instrumental mags and PS1 calibrators [mag]
    clrcoeff = Linear color coefficient from calibration
    clrcoeffunc = 1-sigma uncertainty on clrcoeff
    maglim = Magnitude limit of the science image [mag]
    airmass = Airmass of science image
    nps1matches = Number of PS1 calibrators used in initial calibration of sci image
    """
    id = models.IntegerField(primary_key=True)
    bjd = models.DecimalField(
        max_digits=100, decimal_places=10, null=True)
    mag = models.DecimalField(
        max_digits=100, decimal_places=5, null=True)
    magerr = models.DecimalField(
        max_digits=20, decimal_places=15, null=True)
    diffimflux = models.DecimalField(
        max_digits=100, decimal_places=5, null=True)
    diffimfluxunc = models.DecimalField(
        max_digits=100, decimal_places=5, null=True)
    flag = models.IntegerField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    filterid = models.IntegerField(
        validators=[MaxValueValidator(3), MinValueValidator(1)])
    # TODO: change this one to time
    exptime = models.CharField(max_length=100, null=True)
    pid = models.IntegerField(
        validators=[MaxValueValidator(3), MinValueValidator(1)])
    field = models.IntegerField()
    ccd = models.IntegerField(
        validators=[MaxValueValidator(16), MinValueValidator(1)])
    quad = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)])
    status = models.IntegerField(
        validators=[MaxValueValidator(1), MinValueValidator(0)])
    infobits = models.DecimalField(
        max_digits=100, decimal_places=10)
    seeing = models.DecimalField(
        max_digits=100, decimal_places=10, null=True)
    zpmagsci = models.DecimalField(
        max_digits=101, decimal_places=100, null=True)
    zpmagsciunc = models.DecimalField(
        max_digits=101, decimal_places=100, null=True)
    zpmagscirms = models.DecimalField(
        max_digits=101, decimal_places=100, null=True)
    clrcoeff = models.DecimalField(
        max_digits=101, decimal_places=100, null=True)
    clrcoeffunc = models.DecimalField(
        max_digits=101, decimal_places=100, null=True)
    maglim = models.DecimalField(
        max_digits=100, decimal_places=10, null=True)
    airmass = models.DecimalField(
        max_digits=100, decimal_places=10, null=True)
    nps1matches = models.IntegerField(null=True)

    def __str__(self):
        return self.bjd
    
    class Meta:
        ordering = [models.F('bjd').desc(nulls_last=True)]

