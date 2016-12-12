import hashlib
import os
import unittest

from .. import AjaxUploadTestCase


class BackendTestCase(AjaxUploadTestCase):
    upload_url = None

    def setUp(self):
        if not self.upload_url:
            raise unittest.SkipTest("need an upload url to test backends")
        super(BackendTestCase, self).setUp()

    def test_upload_raw_post(self):
        """
        tests uploading a file in the body of the request
        """
        uploaded_file_name = 'foo.png'
        # post raw self.test_file data to AjaxFileUploader as Ajax
        self.client.post(
            '{}?qqfile={}'.format(self.upload_url, uploaded_file_name),
            self.test_file_data,
            content_type='application/octet-stream',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        uploaded_file_path = os.path.join(
        self.uploads_dir, uploaded_file_name)

        with open(uploaded_file_path, 'rb') as uploaded_file:
            # uploaded file must exist in MEDIA_DIR
            self.assertTrue(os.path.exists(uploaded_file_path))

            # sha1 hash of original file and uploaded file must match
            self.assertEquals(
                hashlib.sha1(uploaded_file.read()).hexdigest(),
                self.test_file_hash
            )
            self.extra_tests()

    def test_upload_ajax_form(self):
        """
        tests uploading a file in FILES
        """
        uploaded_file_name = 'foo.png'
        # post test file file to AjaxFileUploader as Ajax form request
        with open(self.test_file_path, 'rb') as test_file:
            self.client.post(
                self.upload_url,
                {'qqfile': test_file, 'qqfilename': uploaded_file_name},
                HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )
        uploaded_file_path = os.path.join(
            self.uploads_dir, uploaded_file_name)

        with open(uploaded_file_path, 'rb') as uploaded_file:
            # uploaded file must exist in MEDIA_DIR
            self.assertTrue(os.path.exists(uploaded_file_path))

            # sha1 hash of original file and uploaded file must match
            self.assertEquals(
                hashlib.sha1(uploaded_file.read()).hexdigest(),
                self.test_file_hash
            )
            self.extra_tests()

    def extra_tests(self):
        """
        Subclasses can add extra tests here
        """
        pass
