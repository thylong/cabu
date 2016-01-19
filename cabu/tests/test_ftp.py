# -*- coding: utf-8 -*-

from cabu.tests.test_base import TestBase


class TestFtp(TestBase):
    def test_ftp_put_text(self):
        self.ftp.put(None, 'test.txt', contents=b'blah blah blah')
