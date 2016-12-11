from django.conf.urls import include, url

from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.backends.default_storage import DefaultStorageUploadBackend


default_storage_uploader = AjaxFileUploader(backend=DefaultStorageUploadBackend)

urlpatterns = [
    url(r'^upload$', default_storage_uploader, name="ajax-upload-default-storage"),
    url(r'', include('ajaxuploader.urls')),
]
