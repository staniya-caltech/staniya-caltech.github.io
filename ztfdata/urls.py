### data/urls.py ###
from django.urls import path
from django.conf.urls import url
from .views import UploadView
urlpatterns = [
    path('upload/', UploadView, name='upload'),
]
