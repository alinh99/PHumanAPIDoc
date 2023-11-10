# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
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

        Get Total Hour Salary
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

        Get Detail Hour Salary
        """
        query_string = [('id', 28)]
        response = self.client.open(
            '/api/v1//hour/detail-salary/{employeeId}/list'.format(employee_id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_productivity_sum_employee_id_calculation_get(self):
        """Test case for productivity_sum_employee_id_calculation_get

        Calculate productivity
        """
        response = self.client.open(
            '/api/v1//productivity/sum/{employeeId}/calculation'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_productivity_sum_salary_employee_id_calculation_get(self):
        """Test case for productivity_sum_salary_employee_id_calculation_get

        Calculate Salary by productivity
        """
        response = self.client.open(
            '/api/v1//productivity/sum-salary/{employeeId}/calculation'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_productivity_sum_salary_employee_id_list_get(self):
        """Test case for productivity_sum_salary_employee_id_list_get

        Get Sum Salary based on Productivity
        """
        response = self.client.open(
            '/api/v1//productivity/sum-salary/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
