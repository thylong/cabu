# -*- coding: utf-8 -*-

from cabu.tests.test_base import TestBase
from cabu.utils.bucket import Bucket
import unittest


class TestBucket(TestBase):
    @unittest.skip('Wait for a fix in fake-s3')
    def test_crud(self):
        bucket_name = self.app.config.get('S3_BUCKET', '')
        access_key = self.app.config.get('S3_ACCESS_KEY', '')
        secret_key = self.app.config.get('S3_SECRET_KEY', '')
        self.bucket = Bucket(bucket_name, access_key, secret_key)

        r = self.bucket.put(filename='test.txt', data='Test !')
        self.assertEqual(r.status_code, 200)

        r = self.bucket.get(filename='test.txt')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, 'Test !')

        r = self.bucket.delete(filename='test.txt')
        self.assertEqual(r.status_code, 204)
