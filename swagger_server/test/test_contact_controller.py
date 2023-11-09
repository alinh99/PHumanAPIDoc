# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContactController(BaseTestCase):
    """ContactController integration test stubs"""

    def test_employee_employee_id_list_get(self):
        """Test case for employee_employee_id_list_get

        Get Remaining Leaves
        """
        response = self.client.open(
            '/api/v1//employee/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
