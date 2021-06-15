# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.28.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1formSubscription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_date': 'str',
        'end_date': 'str',
        'periodicity': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'periodicity': 'periodicity'
    }

    def __init__(self, start_date=None, end_date=None, periodicity=None):  # noqa: E501
        """V1formSubscription - a model defined in Swagger"""  # noqa: E501
        self._start_date = None
        self._end_date = None
        self._periodicity = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if periodicity is not None:
            self.periodicity = periodicity

    @property
    def start_date(self):
        """Gets the start_date of this V1formSubscription.  # noqa: E501

        First day of subscription  # noqa: E501

        :return: The start_date of this V1formSubscription.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this V1formSubscription.

        First day of subscription  # noqa: E501

        :param start_date: The start_date of this V1formSubscription.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this V1formSubscription.  # noqa: E501

        Last day of subscription  # noqa: E501

        :return: The end_date of this V1formSubscription.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this V1formSubscription.

        Last day of subscription  # noqa: E501

        :param end_date: The end_date of this V1formSubscription.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def periodicity(self):
        """Gets the periodicity of this V1formSubscription.  # noqa: E501

        In days, frequency between purchases  # noqa: E501

        :return: The periodicity of this V1formSubscription.  # noqa: E501
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity):
        """Sets the periodicity of this V1formSubscription.

        In days, frequency between purchases  # noqa: E501

        :param periodicity: The periodicity of this V1formSubscription.  # noqa: E501
        :type: str
        """

        self._periodicity = periodicity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1formSubscription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1formSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
