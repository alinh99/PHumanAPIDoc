import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.models.inline_response5001 import InlineResponse5001  # noqa: E501
from swagger_server import util


def leave_employee_id_list_get(employee_id):  # noqa: E501
    """Returns an employee&#x27;s list of leave applications.

     # noqa: E501

    :param employee_id: Parameter description in CommonMark or HTML.
    :type employee_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def leave_state_list_get():  # noqa: E501
    """Get Leave State List

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def leave_time_list_get():  # noqa: E501
    """Get Time List

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def leave_type_list_get():  # noqa: E501
    """Get Leave Type List

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def productivity_detail_salary_employee_id_list_get(employee_id, id):  # noqa: E501
    """Get Remaining Leaves

     # noqa: E501

    :param employee_id: 
    :type employee_id: int
    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def remaining_leave_employee_id_list_get(employee_id, id):  # noqa: E501
    """Get Remaining Leaves

     # noqa: E501

    :param employee_id: 
    :type employee_id: int
    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'
