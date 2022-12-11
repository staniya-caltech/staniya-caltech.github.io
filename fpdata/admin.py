### data/admin.py ###
from django.contrib import admin
from .models import ZTFFPSData, MROZData, AndrewData

admin.site.register(ZTFFPSData)
admin.site.register(MROZData)
admin.site.register(AndrewData)