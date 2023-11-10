import connexion
import six

from swagger_server.models.inline_response4002 import InlineResponse4002  # noqa: E501
from swagger_server.models.inline_response4003 import InlineResponse4003  # noqa: E501
from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server import util


def check_in_employee_id_add_post(employee_id, checkin_latitude, checkin_longitude, x_img_url_checkin):  # noqa: E501
    """Add an Employee&#x27;s Check-in

     # noqa: E501

    :param employee_id: Parameter description in CommonMark or HTML.
    :type employee_id: int
    :param checkin_latitude: Parameter description in CommonMark or HTML.
    :type checkin_latitude: int
    :param checkin_longitude: Parameter description in CommonMark or HTML.
    :type checkin_longitude: int
    :param x_img_url_checkin: Parameter description in CommonMark or HTML.
    :type x_img_url_checkin: int

    :rtype: None
    """
    return 'do some magic!'


def check_out_employee_id_add_post(employee_id, checkout_latitude, checkout_longitude, x_img_url_checkout):  # noqa: E501
    """Add an Employee&#x27;s Check-in

     # noqa: E501

    :param employee_id: Parameter description in CommonMark or HTML.
    :type employee_id: int
    :param checkout_latitude: Parameter description in CommonMark or HTML.
    :type checkout_latitude: int
    :param checkout_longitude: Parameter description in CommonMark or HTML.
    :type checkout_longitude: int
    :param x_img_url_checkout: Parameter description in CommonMark or HTML.
    :type x_img_url_checkout: int

    :rtype: None
    """
    return 'do some magic!'
