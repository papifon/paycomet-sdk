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

class V1paymentsorderrefundPayment(object):
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
        'terminal': 'int',
        'amount': 'str',
        'currency': 'str',
        'auth_code': 'str',
        'original_ip': 'str',
        'token_user': 'str',
        'id_user': 'int',
        'notify_direct_payment': 'int'
    }

    attribute_map = {
        'terminal': 'terminal',
        'amount': 'amount',
        'currency': 'currency',
        'auth_code': 'authCode',
        'original_ip': 'originalIp',
        'token_user': 'tokenUser',
        'id_user': 'idUser',
        'notify_direct_payment': 'notifyDirectPayment'
    }

    def __init__(self, terminal=None, amount=None, currency=None, auth_code=None, original_ip=None, token_user=None, id_user=None, notify_direct_payment=None):  # noqa: E501
        """V1paymentsorderrefundPayment - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._amount = None
        self._currency = None
        self._auth_code = None
        self._original_ip = None
        self._token_user = None
        self._id_user = None
        self._notify_direct_payment = None
        self.discriminator = None
        self.terminal = terminal
        self.amount = amount
        self.currency = currency
        self.auth_code = auth_code
        self.original_ip = original_ip
        if token_user is not None:
            self.token_user = token_user
        if id_user is not None:
            self.id_user = id_user
        if notify_direct_payment is not None:
            self.notify_direct_payment = notify_direct_payment

    @property
    def terminal(self):
        """Gets the terminal of this V1paymentsorderrefundPayment.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1paymentsorderrefundPayment.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def amount(self):
        """Gets the amount of this V1paymentsorderrefundPayment.  # noqa: E501

        Amount to refund in number format. If empty, total refund asumed.  # noqa: E501

        :return: The amount of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1paymentsorderrefundPayment.

        Amount to refund in number format. If empty, total refund asumed.  # noqa: E501

        :param amount: The amount of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this V1paymentsorderrefundPayment.  # noqa: E501

        Currency of the transaction  # noqa: E501

        :return: The currency of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this V1paymentsorderrefundPayment.

        Currency of the transaction  # noqa: E501

        :param currency: The currency of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def auth_code(self):
        """Gets the auth_code of this V1paymentsorderrefundPayment.  # noqa: E501

         Original bank code of the authorization of the transaction.  # noqa: E501

        :return: The auth_code of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this V1paymentsorderrefundPayment.

         Original bank code of the authorization of the transaction.  # noqa: E501

        :param auth_code: The auth_code of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: str
        """
        if auth_code is None:
            raise ValueError("Invalid value for `auth_code`, must not be `None`")  # noqa: E501

        self._auth_code = auth_code

    @property
    def original_ip(self):
        """Gets the original_ip of this V1paymentsorderrefundPayment.  # noqa: E501

        IP Address of the application of the business.  # noqa: E501

        :return: The original_ip of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: str
        """
        return self._original_ip

    @original_ip.setter
    def original_ip(self, original_ip):
        """Sets the original_ip of this V1paymentsorderrefundPayment.

        IP Address of the application of the business.  # noqa: E501

        :param original_ip: The original_ip of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: str
        """
        if original_ip is None:
            raise ValueError("Invalid value for `original_ip`, must not be `None`")  # noqa: E501

        self._original_ip = original_ip

    @property
    def token_user(self):
        """Gets the token_user of this V1paymentsorderrefundPayment.  # noqa: E501

        Token code associated with the IdUser.  # noqa: E501

        :return: The token_user of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this V1paymentsorderrefundPayment.

        Token code associated with the IdUser.  # noqa: E501

        :param token_user: The token_user of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: str
        """

        self._token_user = token_user

    @property
    def id_user(self):
        """Gets the id_user of this V1paymentsorderrefundPayment.  # noqa: E501

        Unique identifier of the user registered in the system.  # noqa: E501

        :return: The id_user of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this V1paymentsorderrefundPayment.

        Unique identifier of the user registered in the system.  # noqa: E501

        :param id_user: The id_user of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: int
        """

        self._id_user = id_user

    @property
    def notify_direct_payment(self):
        """Gets the notify_direct_payment of this V1paymentsorderrefundPayment.  # noqa: E501

        Configurate POST notification of the operation result (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed  # noqa: E501

        :return: The notify_direct_payment of this V1paymentsorderrefundPayment.  # noqa: E501
        :rtype: int
        """
        return self._notify_direct_payment

    @notify_direct_payment.setter
    def notify_direct_payment(self, notify_direct_payment):
        """Sets the notify_direct_payment of this V1paymentsorderrefundPayment.

        Configurate POST notification of the operation result (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed  # noqa: E501

        :param notify_direct_payment: The notify_direct_payment of this V1paymentsorderrefundPayment.  # noqa: E501
        :type: int
        """

        self._notify_direct_payment = notify_direct_payment

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
        if issubclass(V1paymentsorderrefundPayment, dict):
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
        if not isinstance(other, V1paymentsorderrefundPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
