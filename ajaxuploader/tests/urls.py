from django.conf.urls import include, url

from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.backends.default_storage import DefaultStorageUploadBackend
from ajaxuploader.backends.local import LocalUploadBackend
from ajaxuploader.backends.thumbnail import ThumbnailUploadBackend
from ajaxuploader.backends.easythumbnails import EasyThumbnailUploadBackend


class CustomThumbnailUploadBackend(ThumbnailUploadBackend):
    KEEP_ORIGINAL = True


class CustomEasyThumbnailUploadBackend(EasyThumbnailUploadBackend):
    KEEP_ORIGINAL = True


urlpatterns = [
    url(
        r'^upload-default$',
        AjaxFileUploader(backend=DefaultStorageUploadBackend),
        name="ajax-upload-default-storage"
    ),
    url(
        r'^upload-local$',
        AjaxFileUploader(backend=LocalUploadBackend),
        name="ajax-upload-local-storage"
    ),
    url(
        r'^upload-thumbnail$',
        AjaxFileUploader(backend=CustomThumbnailUploadBackend),
        name="ajax-upload-thumbnail-storage"
    ),
    url(
        r'^upload-easy-thumbnails$',
        AjaxFileUploader(backend=CustomEasyThumbnailUploadBackend),
        name="ajax-upload-easy-thumbnails-storage"
    ),
    # Base ajaxuploader URLs
    url(r'', include('ajaxuploader.urls')),
]
