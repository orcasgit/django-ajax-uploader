from django.core.urlresolvers import reverse

from . import BackendTestCase


class DefaultStorageTest(BackendTestCase):
    upload_url = reverse('ajax-upload-default-storage')
