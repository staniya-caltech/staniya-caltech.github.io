from django.urls import path
from .views import UploadView, DataView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", UploadView, name="upload"),
    path("table/", DataView, name="table"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.PHOT_URL, document_root=settings.PHOT_ROOT)
