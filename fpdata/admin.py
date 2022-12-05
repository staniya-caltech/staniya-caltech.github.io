### data/admin.py ###
from django.contrib import admin
from .models import ZTFFPSData, MROZData

admin.site.register(ZTFFPSData)
admin.site.register(MROZData)