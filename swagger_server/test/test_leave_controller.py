# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLeaveController(BaseTestCase):
    """LeaveController integration test stubs"""

    def test_leave_employee_id_list_get(self):
        """Test case for leave_employee_id_list_get

        Returns an employee's list of leave applications.
        """
        response = self.client.open(
            '/api/v1//leave/{employeeId}/list'.format(employee_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_leave_state_list_get(self):
        """Test case for leave_state_list_get

        Get Leave State List
        """
        response = self.client.open(
            '/api/v1//leave/state/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_leave_time_list_get(self):
        """Test case for leave_time_list_get

        Get Time List
        """
        response = self.client.open(
            '/api/v1//leave/time/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_leave_type_list_get(self):
        """Test case for leave_type_list_get

        Get Leave Type List
        """
        response = self.client.open(
            '/api/v1//leave-type/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remaining_leave_employee_id_list_get(self):
        """Test case for remaining_leave_employee_id_list_get

        Get Remaining Leaves
        """
        query_string = [('id', 1)]
        response = self.client.open(
            '/api/v1//remaining-leave/{employeeId}/list'.format(employee_id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
