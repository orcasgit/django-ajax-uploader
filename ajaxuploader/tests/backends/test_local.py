from django.core.urlresolvers import reverse

from . import BackendTestCase


class LocalStorageTest(BackendTestCase):
    upload_url = reverse('ajax-upload-local-storage')
