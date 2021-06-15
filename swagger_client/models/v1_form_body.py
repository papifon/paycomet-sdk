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

class V1FormBody(object):
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
        'operation_type': 'int',
        'language': 'str',
        'terminal': 'int',
        'product_description': 'str',
        'payment': 'V1formPayment',
        'subscription': 'V1formSubscription'
    }

    attribute_map = {
        'operation_type': 'operationType',
        'language': 'language',
        'terminal': 'terminal',
        'product_description': 'productDescription',
        'payment': 'payment',
        'subscription': 'subscription'
    }

    def __init__(self, operation_type=None, language=None, terminal=None, product_description=None, payment=None, subscription=None):  # noqa: E501
        """V1FormBody - a model defined in Swagger"""  # noqa: E501
        self._operation_type = None
        self._language = None
        self._terminal = None
        self._product_description = None
        self._payment = None
        self._subscription = None
        self.discriminator = None
        self.operation_type = operation_type
        if language is not None:
            self.language = language
        if terminal is not None:
            self.terminal = terminal
        if product_description is not None:
            self.product_description = product_description
        if payment is not None:
            self.payment = payment
        if subscription is not None:
            self.subscription = subscription

    @property
    def operation_type(self):
        """Gets the operation_type of this V1FormBody.  # noqa: E501

        PAYCOMET operation type (ID 1 - authorization, 3 - preauthorization, 9 - subscription, 107 - tokenization, 114 - authorization by reference, 116 - dcc authorization).  # noqa: E501

        :return: The operation_type of this V1FormBody.  # noqa: E501
        :rtype: int
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this V1FormBody.

        PAYCOMET operation type (ID 1 - authorization, 3 - preauthorization, 9 - subscription, 107 - tokenization, 114 - authorization by reference, 116 - dcc authorization).  # noqa: E501

        :param operation_type: The operation_type of this V1FormBody.  # noqa: E501
        :type: int
        """
        if operation_type is None:
            raise ValueError("Invalid value for `operation_type`, must not be `None`")  # noqa: E501

        self._operation_type = operation_type

    @property
    def language(self):
        """Gets the language of this V1FormBody.  # noqa: E501

        Language for user interface.  # noqa: E501

        :return: The language of this V1FormBody.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V1FormBody.

        Language for user interface.  # noqa: E501

        :param language: The language of this V1FormBody.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def terminal(self):
        """Gets the terminal of this V1FormBody.  # noqa: E501

        Product or terminal Id  # noqa: E501

        :return: The terminal of this V1FormBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1FormBody.

        Product or terminal Id  # noqa: E501

        :param terminal: The terminal of this V1FormBody.  # noqa: E501
        :type: int
        """

        self._terminal = terminal

    @property
    def product_description(self):
        """Gets the product_description of this V1FormBody.  # noqa: E501

        Product description (only in 107 - tokenization).  # noqa: E501

        :return: The product_description of this V1FormBody.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this V1FormBody.

        Product description (only in 107 - tokenization).  # noqa: E501

        :param product_description: The product_description of this V1FormBody.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def payment(self):
        """Gets the payment of this V1FormBody.  # noqa: E501


        :return: The payment of this V1FormBody.  # noqa: E501
        :rtype: V1formPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this V1FormBody.


        :param payment: The payment of this V1FormBody.  # noqa: E501
        :type: V1formPayment
        """

        self._payment = payment

    @property
    def subscription(self):
        """Gets the subscription of this V1FormBody.  # noqa: E501


        :return: The subscription of this V1FormBody.  # noqa: E501
        :rtype: V1formSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this V1FormBody.


        :param subscription: The subscription of this V1FormBody.  # noqa: E501
        :type: V1formSubscription
        """

        self._subscription = subscription

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
        if issubclass(V1FormBody, dict):
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
        if not isinstance(other, V1FormBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
