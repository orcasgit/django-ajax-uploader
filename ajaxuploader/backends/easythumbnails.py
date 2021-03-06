import os

from django.conf import settings
from easy_thumbnails.files import get_thumbnailer

from ajaxuploader.backends.local import LocalUploadBackend


class EasyThumbnailUploadBackend(LocalUploadBackend):
    DIMENSIONS = (100, 100)
    CROP = True
    KEEP_ORIGINAL = False

    def upload_complete(self, request, filename, *args, **kwargs):

        options = {'size': self.DIMENSIONS, 'crop': self.CROP}
        thumb = get_thumbnailer(self._path).get_thumbnail(options)

        if not self.KEEP_ORIGINAL:
            os.unlink(self._path)

        return {"path": settings.MEDIA_URL + self.UPLOAD_DIR + '/' + os.path.split(thumb.path)[1]}
