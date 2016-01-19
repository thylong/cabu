# -*- coding: utf-8 -*-

from flask import Response
from cabu.tests.test_base import TestBase
from cabu.auth import check_auth, authenticate


class TestAuth(TestBase):
    def test_check_auth(self):
        with self.app.test_request_context():
            self.assertTrue(check_auth('admin', 'admin'))
            self.assertFalse(check_auth('admin', 'nonadmin'))

    def test_authenticate(self):
        response = authenticate()
        self.assertIsInstance(response, Response)
        status_code, message = self.parse_response(response)
        self.assertEquals(401, 401)
