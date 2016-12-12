import json
import os

from django.conf import settings
from django.core.urlresolvers import reverse

from easy_thumbnails.files import get_thumbnailer

from . import BackendTestCase


class EasyThumbnailsStorageTest(BackendTestCase):
    upload_url = reverse('ajax-upload-easy-thumbnails-storage')

    def extra_tests(self):
        with self.assertNumQueries(0):
            options = {'size': (100, 100), 'crop': True}
            thumb = get_thumbnailer('uploads/foo.png').get_thumbnail(options)
            thumbnail_path = os.path.join(
                settings.MEDIA_ROOT,
                'uploads',
                os.path.split(thumb.path)[1]
            )

            self.assertTrue(os.path.exists(thumbnail_path))
