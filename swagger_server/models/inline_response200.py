# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result: List[object]=None, message: str='Your leave applications run successfully', success: bool=True):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param result: The result of this InlineResponse200.  # noqa: E501
        :type result: List[object]
        :param message: The message of this InlineResponse200.  # noqa: E501
        :type message: str
        :param success: The success of this InlineResponse200.  # noqa: E501
        :type success: bool
        """
        self.swagger_types = {
            'result': List[object],
            'message': str,
            'success': bool
        }

        self.attribute_map = {
            'result': 'result',
            'message': 'message',
            'success': 'success'
        }
        self._result = result
        self._message = message
        self._success = success

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> List[object]:
        """Gets the result of this InlineResponse200.


        :return: The result of this InlineResponse200.
        :rtype: List[object]
        """
        return self._result

    @result.setter
    def result(self, result: List[object]):
        """Sets the result of this InlineResponse200.


        :param result: The result of this InlineResponse200.
        :type result: List[object]
        """

        self._result = result

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse200.


        :return: The message of this InlineResponse200.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse200.


        :param message: The message of this InlineResponse200.
        :type message: str
        """

        self._message = message

    @property
    def success(self) -> bool:
        """Gets the success of this InlineResponse200.


        :return: The success of this InlineResponse200.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this InlineResponse200.


        :param success: The success of this InlineResponse200.
        :type success: bool
        """

        self._success = success