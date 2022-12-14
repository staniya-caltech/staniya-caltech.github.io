# Generated by Django 3.2.6 on 2023-01-10 22:36

import django.core.validators
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AndrewData',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('PS1_ID', models.BigIntegerField()),
                ('MJD', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('Mag_ZTF', models.DecimalField(decimal_places=5, max_digits=100, null=True)),
                ('Mag_err', models.DecimalField(decimal_places=15, max_digits=20, null=True)),
                ('Flux', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('Flux_err', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('g_PS1', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('r_PS1', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('i_PS1', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('Stargal', models.DecimalField(decimal_places=15, max_digits=20, null=True)),
                ('infobits', models.IntegerField(null=True)),
            ],
            options={
                'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('MJD'), descending=True, nulls_last=True)],
            },
        ),
        migrations.CreateModel(
            name='MROZData',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('bjd', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('mag', models.DecimalField(decimal_places=5, max_digits=100, null=True)),
                ('magerr', models.DecimalField(decimal_places=15, max_digits=20, null=True)),
                ('diffimflux', models.DecimalField(decimal_places=5, max_digits=100, null=True)),
                ('diffimfluxunc', models.DecimalField(decimal_places=5, max_digits=100, null=True)),
                ('flag', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('filterid', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('exptime', models.CharField(max_length=100, null=True)),
                ('pid', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('field', models.IntegerField()),
                ('ccd', models.IntegerField(validators=[django.core.validators.MaxValueValidator(16), django.core.validators.MinValueValidator(1)])),
                ('quad', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('status', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('infobits', models.DecimalField(decimal_places=10, max_digits=100)),
                ('seeing', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('zpmagsci', models.DecimalField(decimal_places=100, max_digits=101, null=True)),
                ('zpmagsciunc', models.DecimalField(decimal_places=100, max_digits=101, null=True)),
                ('zpmagscirms', models.DecimalField(decimal_places=100, max_digits=101, null=True)),
                ('clrcoeff', models.DecimalField(decimal_places=100, max_digits=101, null=True)),
                ('clrcoeffunc', models.DecimalField(decimal_places=100, max_digits=101, null=True)),
                ('maglim', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('airmass', models.DecimalField(decimal_places=10, max_digits=100, null=True)),
                ('nps1matches', models.IntegerField(null=True)),
            ],
            options={
                'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('bjd'), descending=True, nulls_last=True)],
            },
        ),
        migrations.CreateModel(
            name='ZTFFPSData',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('field', models.IntegerField()),
                ('ccdid', models.IntegerField()),
                ('qid', models.IntegerField()),
                ('filter', models.CharField(max_length=5)),
                ('pid', models.BigIntegerField(null=True)),
                ('infobitssci', models.IntegerField(null=True)),
                ('sciinpseeing', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('scibckgnd', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('scisigpix', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('zpmaginpsci', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('zpmaginpsciunc', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('zpmaginpscirms', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('clrcoeff', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('clrcoeffunc', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('ncalmatches', models.IntegerField(null=True)),
                ('exptime', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('adpctdif1', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('adpctdif2', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('diffmaglim', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('zpdiff', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('programid', models.IntegerField(null=True)),
                ('jd', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('rfid', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimflux', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimfluxunc', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimsnr', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimchisq', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimfluxap', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimfluxuncap', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('forcediffimsnrap', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('aperturecorr', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('dnearestrefsrc', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('nearestrefmag', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('nearestrefmagunc', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('nearestrefchi', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('nearestrefsharp', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('refjdstart', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('refjdend', models.DecimalField(decimal_places=15, max_digits=100, null=True)),
                ('procstatus', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('jd'), descending=True, nulls_last=True)],
            },
        ),
    ]
