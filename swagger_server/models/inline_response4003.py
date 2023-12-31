# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse4003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message: str='checkout_latitude/checkout_longitude/x_img_url_checkout is required', success: bool=False):  # noqa: E501
        """InlineResponse4003 - a model defined in Swagger

        :param message: The message of this InlineResponse4003.  # noqa: E501
        :type message: str
        :param success: The success of this InlineResponse4003.  # noqa: E501
        :type success: bool
        """
        self.swagger_types = {
            'message': str,
            'success': bool
        }

        self.attribute_map = {
            'message': 'message',
            'success': 'success'
        }
        self._message = message
        self._success = success

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse4003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400_3 of this InlineResponse4003.  # noqa: E501
        :rtype: InlineResponse4003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse4003.


        :return: The message of this InlineResponse4003.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse4003.


        :param message: The message of this InlineResponse4003.
        :type message: str
        """

        self._message = message

    @property
    def success(self) -> bool:
        """Gets the success of this InlineResponse4003.


        :return: The success of this InlineResponse4003.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this InlineResponse4003.


        :param success: The success of this InlineResponse4003.
        :type success: bool
        """

        self._success = success
