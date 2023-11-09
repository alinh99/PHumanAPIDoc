# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPayrollController(BaseTestCase):
    """PayrollController integration test stubs"""

    def test_payroll_detail_employee_id_list_get(self):
        """Test case for payroll_detail_employee_id_list_get

        Get Payroll List Details
        """
        response = self.client.open(
            '/api/v1//payroll-detail/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_payroll_employee_idlist_get(self):
        """Test case for payroll_employee_idlist_get

        Get Payroll List
        """
        response = self.client.open(
            '/api/v1//payroll/{employeeId}list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
