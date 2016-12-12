import json
import os

from django.conf import settings
from django.core.urlresolvers import reverse

from sorl.thumbnail import get_thumbnail

from . import BackendTestCase


class ThumbnailStorageTest(BackendTestCase):
    upload_url = reverse('ajax-upload-thumbnail-storage')

    def extra_tests(self):
        with self.assertNumQueries(0):
            thumbnail = get_thumbnail('uploads/foo.png', '100x100')
            thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail.name)

            self.assertTrue(os.path.exists(thumbnail_path))
