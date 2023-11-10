# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response4002 import InlineResponse4002  # noqa: E501
from swagger_server.models.inline_response4003 import InlineResponse4003  # noqa: E501
from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAttendanceController(BaseTestCase):
    """AttendanceController integration test stubs"""

    def test_check_in_employee_id_add_post(self):
        """Test case for check_in_employee_id_add_post

        Add an Employee's Check-in
        """
        query_string = [('checkin_latitude', 56),
                        ('checkin_longitude', 56),
                        ('x_img_url_checkin', 789)]
        response = self.client.open(
            '/api/v1//check-in/{employeeId}/add'.format(employee_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_check_out_employee_id_add_post(self):
        """Test case for check_out_employee_id_add_post

        Add an Employee's Check-in
        """
        query_string = [('checkout_latitude', 56),
                        ('checkout_longitude', 56),
                        ('x_img_url_checkout', 789)]
        response = self.client.open(
            '/api/v1//check-out/{employeeId}/add'.format(employee_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
