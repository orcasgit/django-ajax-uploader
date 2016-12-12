import hashlib
import os
from shutil import rmtree

from django.conf import settings
from django.test import TestCase


class AjaxUploadTestCase(TestCase):
    def setUp(self):
        super(AjaxUploadTestCase, self).setUp()

        self.uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        if not os.path.isdir(self.uploads_dir):
            os.makedirs(self.uploads_dir)

        test_dir = os.path.dirname(__file__)
        self.test_file_path = os.path.join(
            test_dir, '../fixtures/pony.png')
        with open(self.test_file_path, 'rb') as test_file:
            # generate sha1 hash of the file
            self.test_file_data = test_file.read()
            self.test_file_hash = hashlib.sha1(
                self.test_file_data
            ).hexdigest()

    def tearDown(self):
        # remove created uploads/tests directory
        rmtree(self.uploads_dir)
