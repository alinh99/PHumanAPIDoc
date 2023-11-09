# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSalaryController(BaseTestCase):
    """SalaryController integration test stubs"""

    def test_hour_all_salary_employee_id_calculation_get(self):
        """Test case for hour_all_salary_employee_id_calculation_get

        Calculate Sum of Salary Based on Hours
        """
        response = self.client.open(
            '/api/v1//hour/all-salary/{employeeId}/calculation'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hour_all_salary_employee_id_list_get(self):
        """Test case for hour_all_salary_employee_id_list_get

        Get Hour Salaries
        """
        response = self.client.open(
            '/api/v1//hour/all-salary/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hour_detail_salary_employee_id_calculation_get(self):
        """Test case for hour_detail_salary_employee_id_calculation_get

        Calculate Detail Salary Based on Hours
        """
        response = self.client.open(
            '/api/v1//hour/detail-salary/{employeeId}/calculation'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hour_detail_salary_employee_id_list_get(self):
        """Test case for hour_detail_salary_employee_id_list_get

        Get Hour Salaries
        """
        response = self.client.open(
            '/api/v1//hour/detail-salary/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
