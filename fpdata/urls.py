### data/urls.py ###
from django.urls import path
from django.conf.urls import url
from .views import UploadView, DataView
urlpatterns = [
    path('upload/', UploadView, name='upload'),  # type: ignore
    path('table/', DataView, name='table'),
]
