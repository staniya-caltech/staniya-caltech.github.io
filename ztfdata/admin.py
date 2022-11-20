### data/admin.py ###
from django.contrib import admin
from .models import PandasData

admin.site.register(PandasData)