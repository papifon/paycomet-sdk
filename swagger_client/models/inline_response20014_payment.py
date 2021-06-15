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

class InlineResponse20014Payment(object):
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
        'operation_id': 'int',
        'method_id': 'int',
        'timestamp': 'str',
        'order': 'str',
        'operation_type': 'int',
        'operation_name': 'str',
        'state': 'int',
        'state_name': 'str',
        'response': 'str',
        'terminal': 'int',
        'terminal_name': 'str',
        'user': 'str',
        'amount': 'str',
        'currency': 'str',
        'amount_display': 'str',
        'error_code': 'int',
        'error_description': 'str',
        'fee_euro': 'float',
        'fee_percent': 'float',
        'original_ip': 'str',
        'pan': 'str',
        'scoring': 'str',
        'merchant_bank': 'str',
        'bic_code': 'str',
        'product_description': 'str',
        'card_type': 'str',
        'card_category': 'str',
        'card_brand': 'str',
        'card_country': 'str',
        'secure': 'str',
        'split_id': 'int',
        'issuer_bank': 'str',
        'auth_code': 'str',
        'history': 'list[InlineResponse20014PaymentHistory]'
    }

    attribute_map = {
        'operation_id': 'operationId',
        'method_id': 'methodId',
        'timestamp': 'timestamp',
        'order': 'order',
        'operation_type': 'operationType',
        'operation_name': 'operationName',
        'state': 'state',
        'state_name': 'stateName',
        'response': 'response',
        'terminal': 'terminal',
        'terminal_name': 'terminalName',
        'user': 'user',
        'amount': 'amount',
        'currency': 'currency',
        'amount_display': 'amountDisplay',
        'error_code': 'errorCode',
        'error_description': 'errorDescription',
        'fee_euro': 'feeEuro',
        'fee_percent': 'feePercent',
        'original_ip': 'originalIp',
        'pan': 'pan',
        'scoring': 'scoring',
        'merchant_bank': 'merchantBank',
        'bic_code': 'bicCode',
        'product_description': 'productDescription',
        'card_type': 'cardType',
        'card_category': 'cardCategory',
        'card_brand': 'cardBrand',
        'card_country': 'cardCountry',
        'secure': 'secure',
        'split_id': 'splitId',
        'issuer_bank': 'issuerBank',
        'auth_code': 'authCode',
        'history': 'history'
    }

    def __init__(self, operation_id=None, method_id=None, timestamp=None, order=None, operation_type=None, operation_name=None, state=None, state_name=None, response=None, terminal=None, terminal_name=None, user=None, amount=None, currency=None, amount_display=None, error_code=None, error_description=None, fee_euro=None, fee_percent=None, original_ip=None, pan=None, scoring=None, merchant_bank=None, bic_code=None, product_description=None, card_type=None, card_category=None, card_brand=None, card_country=None, secure=None, split_id=None, issuer_bank=None, auth_code=None, history=None):  # noqa: E501
        """InlineResponse20014Payment - a model defined in Swagger"""  # noqa: E501
        self._operation_id = None
        self._method_id = None
        self._timestamp = None
        self._order = None
        self._operation_type = None
        self._operation_name = None
        self._state = None
        self._state_name = None
        self._response = None
        self._terminal = None
        self._terminal_name = None
        self._user = None
        self._amount = None
        self._currency = None
        self._amount_display = None
        self._error_code = None
        self._error_description = None
        self._fee_euro = None
        self._fee_percent = None
        self._original_ip = None
        self._pan = None
        self._scoring = None
        self._merchant_bank = None
        self._bic_code = None
        self._product_description = None
        self._card_type = None
        self._card_category = None
        self._card_brand = None
        self._card_country = None
        self._secure = None
        self._split_id = None
        self._issuer_bank = None
        self._auth_code = None
        self._history = None
        self.discriminator = None
        if operation_id is not None:
            self.operation_id = operation_id
        if method_id is not None:
            self.method_id = method_id
        if timestamp is not None:
            self.timestamp = timestamp
        if order is not None:
            self.order = order
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_name is not None:
            self.operation_name = operation_name
        if state is not None:
            self.state = state
        if state_name is not None:
            self.state_name = state_name
        if response is not None:
            self.response = response
        if terminal is not None:
            self.terminal = terminal
        if terminal_name is not None:
            self.terminal_name = terminal_name
        if user is not None:
            self.user = user
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if amount_display is not None:
            self.amount_display = amount_display
        if error_code is not None:
            self.error_code = error_code
        if error_description is not None:
            self.error_description = error_description
        if fee_euro is not None:
            self.fee_euro = fee_euro
        if fee_percent is not None:
            self.fee_percent = fee_percent
        if original_ip is not None:
            self.original_ip = original_ip
        if pan is not None:
            self.pan = pan
        if scoring is not None:
            self.scoring = scoring
        if merchant_bank is not None:
            self.merchant_bank = merchant_bank
        if bic_code is not None:
            self.bic_code = bic_code
        if product_description is not None:
            self.product_description = product_description
        if card_type is not None:
            self.card_type = card_type
        if card_category is not None:
            self.card_category = card_category
        if card_brand is not None:
            self.card_brand = card_brand
        if card_country is not None:
            self.card_country = card_country
        if secure is not None:
            self.secure = secure
        if split_id is not None:
            self.split_id = split_id
        if issuer_bank is not None:
            self.issuer_bank = issuer_bank
        if auth_code is not None:
            self.auth_code = auth_code
        if history is not None:
            self.history = history

    @property
    def operation_id(self):
        """Gets the operation_id of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET identifier  # noqa: E501

        :return: The operation_id of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this InlineResponse20014Payment.

        PAYCOMET identifier  # noqa: E501

        :param operation_id: The operation_id of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._operation_id = operation_id

    @property
    def method_id(self):
        """Gets the method_id of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET payment method ID. 1 is for card.  # noqa: E501

        :return: The method_id of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this InlineResponse20014Payment.

        PAYCOMET payment method ID. 1 is for card.  # noqa: E501

        :param method_id: The method_id of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._method_id = method_id

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse20014Payment.  # noqa: E501

        Timestamp of transaction  # noqa: E501

        :return: The timestamp of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse20014Payment.

        Timestamp of transaction  # noqa: E501

        :param timestamp: The timestamp of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def order(self):
        """Gets the order of this InlineResponse20014Payment.  # noqa: E501

        Unique reference for merchant's purchase  # noqa: E501

        :return: The order of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse20014Payment.

        Unique reference for merchant's purchase  # noqa: E501

        :param order: The order of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def operation_type(self):
        """Gets the operation_type of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET operation type ID.  # noqa: E501

        :return: The operation_type of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this InlineResponse20014Payment.

        PAYCOMET operation type ID.  # noqa: E501

        :param operation_type: The operation_type of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._operation_type = operation_type

    @property
    def operation_name(self):
        """Gets the operation_name of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET operation type description.  # noqa: E501

        :return: The operation_name of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """Sets the operation_name of this InlineResponse20014Payment.

        PAYCOMET operation type description.  # noqa: E501

        :param operation_name: The operation_name of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._operation_name = operation_name

    @property
    def state(self):
        """Gets the state of this InlineResponse20014Payment.  # noqa: E501

        Identifier of the state of the operation. 0 means operation failed, 1 operation correct.  # noqa: E501

        :return: The state of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse20014Payment.

        Identifier of the state of the operation. 0 means operation failed, 1 operation correct.  # noqa: E501

        :param state: The state of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def state_name(self):
        """Gets the state_name of this InlineResponse20014Payment.  # noqa: E501

        Literal of the state of the operation.  # noqa: E501

        :return: The state_name of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        """Sets the state_name of this InlineResponse20014Payment.

        Literal of the state of the operation.  # noqa: E501

        :param state_name: The state_name of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._state_name = state_name

    @property
    def response(self):
        """Gets the response of this InlineResponse20014Payment.  # noqa: E501

        Status of transation. OK, KO o SF (pending payment).  # noqa: E501

        :return: The response of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this InlineResponse20014Payment.

        Status of transation. OK, KO o SF (pending payment).  # noqa: E501

        :param response: The response of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def terminal(self):
        """Gets the terminal of this InlineResponse20014Payment.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this InlineResponse20014Payment.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._terminal = terminal

    @property
    def terminal_name(self):
        """Gets the terminal_name of this InlineResponse20014Payment.  # noqa: E501

        Customer product name  # noqa: E501

        :return: The terminal_name of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._terminal_name

    @terminal_name.setter
    def terminal_name(self, terminal_name):
        """Sets the terminal_name of this InlineResponse20014Payment.

        Customer product name  # noqa: E501

        :param terminal_name: The terminal_name of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._terminal_name = terminal_name

    @property
    def user(self):
        """Gets the user of this InlineResponse20014Payment.  # noqa: E501

        Administrative user of the operation  # noqa: E501

        :return: The user of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineResponse20014Payment.

        Administrative user of the operation  # noqa: E501

        :param user: The user of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20014Payment.  # noqa: E501

        Amount of the operation in number format. 1.00 EURO = 100, 4.50 EUROS = 450...  # noqa: E501

        :return: The amount of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20014Payment.

        Amount of the operation in number format. 1.00 EURO = 100, 4.50 EUROS = 450...  # noqa: E501

        :param amount: The amount of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InlineResponse20014Payment.  # noqa: E501

        Currency of the transaction.   # noqa: E501

        :return: The currency of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse20014Payment.

        Currency of the transaction.   # noqa: E501

        :param currency: The currency of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount_display(self):
        """Gets the amount_display of this InlineResponse20014Payment.  # noqa: E501

        Literal of the operation amount (with currency symbol)  # noqa: E501

        :return: The amount_display of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._amount_display

    @amount_display.setter
    def amount_display(self, amount_display):
        """Sets the amount_display of this InlineResponse20014Payment.

        Literal of the operation amount (with currency symbol)  # noqa: E501

        :param amount_display: The amount_display of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._amount_display = amount_display

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20014Payment.  # noqa: E501

        Error code given by PAYCOMET.  # noqa: E501

        :return: The error_code of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20014Payment.

        Error code given by PAYCOMET.  # noqa: E501

        :param error_code: The error_code of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def error_description(self):
        """Gets the error_description of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET operation type description.  # noqa: E501

        :return: The error_description of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this InlineResponse20014Payment.

        PAYCOMET operation type description.  # noqa: E501

        :param error_description: The error_description of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def fee_euro(self):
        """Gets the fee_euro of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET fee for the transaction fixed per operation (in euros)  # noqa: E501

        :return: The fee_euro of this InlineResponse20014Payment.  # noqa: E501
        :rtype: float
        """
        return self._fee_euro

    @fee_euro.setter
    def fee_euro(self, fee_euro):
        """Sets the fee_euro of this InlineResponse20014Payment.

        PAYCOMET fee for the transaction fixed per operation (in euros)  # noqa: E501

        :param fee_euro: The fee_euro of this InlineResponse20014Payment.  # noqa: E501
        :type: float
        """

        self._fee_euro = fee_euro

    @property
    def fee_percent(self):
        """Gets the fee_percent of this InlineResponse20014Payment.  # noqa: E501

        PAYCOMET fee for the transaction variable per operation (in euros)  # noqa: E501

        :return: The fee_percent of this InlineResponse20014Payment.  # noqa: E501
        :rtype: float
        """
        return self._fee_percent

    @fee_percent.setter
    def fee_percent(self, fee_percent):
        """Sets the fee_percent of this InlineResponse20014Payment.

        PAYCOMET fee for the transaction variable per operation (in euros)  # noqa: E501

        :param fee_percent: The fee_percent of this InlineResponse20014Payment.  # noqa: E501
        :type: float
        """

        self._fee_percent = fee_percent

    @property
    def original_ip(self):
        """Gets the original_ip of this InlineResponse20014Payment.  # noqa: E501

        IP Address of the customer that initiated the payment transaction  # noqa: E501

        :return: The original_ip of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._original_ip

    @original_ip.setter
    def original_ip(self, original_ip):
        """Sets the original_ip of this InlineResponse20014Payment.

        IP Address of the customer that initiated the payment transaction  # noqa: E501

        :param original_ip: The original_ip of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._original_ip = original_ip

    @property
    def pan(self):
        """Gets the pan of this InlineResponse20014Payment.  # noqa: E501

        Masked credit/debit card  # noqa: E501

        :return: The pan of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._pan

    @pan.setter
    def pan(self, pan):
        """Sets the pan of this InlineResponse20014Payment.

        Masked credit/debit card  # noqa: E501

        :param pan: The pan of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._pan = pan

    @property
    def scoring(self):
        """Gets the scoring of this InlineResponse20014Payment.  # noqa: E501

        Risk scoring value from 0 to 100.  # noqa: E501

        :return: The scoring of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._scoring

    @scoring.setter
    def scoring(self, scoring):
        """Sets the scoring of this InlineResponse20014Payment.

        Risk scoring value from 0 to 100.  # noqa: E501

        :param scoring: The scoring of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._scoring = scoring

    @property
    def merchant_bank(self):
        """Gets the merchant_bank of this InlineResponse20014Payment.  # noqa: E501

        Bank of merchant terminal.  # noqa: E501

        :return: The merchant_bank of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._merchant_bank

    @merchant_bank.setter
    def merchant_bank(self, merchant_bank):
        """Sets the merchant_bank of this InlineResponse20014Payment.

        Bank of merchant terminal.  # noqa: E501

        :param merchant_bank: The merchant_bank of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._merchant_bank = merchant_bank

    @property
    def bic_code(self):
        """Gets the bic_code of this InlineResponse20014Payment.  # noqa: E501

        Biccode of the entity by which the transaction was processed.  # noqa: E501

        :return: The bic_code of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._bic_code

    @bic_code.setter
    def bic_code(self, bic_code):
        """Sets the bic_code of this InlineResponse20014Payment.

        Biccode of the entity by which the transaction was processed.  # noqa: E501

        :param bic_code: The bic_code of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._bic_code = bic_code

    @property
    def product_description(self):
        """Gets the product_description of this InlineResponse20014Payment.  # noqa: E501

        Description of the product sold.  # noqa: E501

        :return: The product_description of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this InlineResponse20014Payment.

        Description of the product sold.  # noqa: E501

        :param product_description: The product_description of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def card_type(self):
        """Gets the card_type of this InlineResponse20014Payment.  # noqa: E501

        Type of card. If it can be identified, information on the type of card will be sent (DEBIT, CREDIT, etc). Otherwise, the field will be returned blank.  # noqa: E501

        :return: The card_type of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this InlineResponse20014Payment.

        Type of card. If it can be identified, information on the type of card will be sent (DEBIT, CREDIT, etc). Otherwise, the field will be returned blank.  # noqa: E501

        :param card_type: The card_type of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def card_category(self):
        """Gets the card_category of this InlineResponse20014Payment.  # noqa: E501

        Category of card. If it can be identified, information on the category of card will be sent. Otherwise, the field will be returned blank.  # noqa: E501

        :return: The card_category of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._card_category

    @card_category.setter
    def card_category(self, card_category):
        """Sets the card_category of this InlineResponse20014Payment.

        Category of card. If it can be identified, information on the category of card will be sent. Otherwise, the field will be returned blank.  # noqa: E501

        :param card_category: The card_category of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._card_category = card_category

    @property
    def card_brand(self):
        """Gets the card_brand of this InlineResponse20014Payment.  # noqa: E501

        Brand of card. If it can be identified, information on the brand of card will be sent. Otherwise, the field will be returned blank.  # noqa: E501

        :return: The card_brand of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._card_brand

    @card_brand.setter
    def card_brand(self, card_brand):
        """Sets the card_brand of this InlineResponse20014Payment.

        Brand of card. If it can be identified, information on the brand of card will be sent. Otherwise, the field will be returned blank.  # noqa: E501

        :param card_brand: The card_brand of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._card_brand = card_brand

    @property
    def card_country(self):
        """Gets the card_country of this InlineResponse20014Payment.  # noqa: E501

        Country of the issuer of the card in ISO3 Code (ex.: 724 = Spain). May be left empty.  # noqa: E501

        :return: The card_country of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._card_country

    @card_country.setter
    def card_country(self, card_country):
        """Sets the card_country of this InlineResponse20014Payment.

        Country of the issuer of the card in ISO3 Code (ex.: 724 = Spain). May be left empty.  # noqa: E501

        :param card_country: The card_country of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._card_country = card_country

    @property
    def secure(self):
        """Gets the secure of this InlineResponse20014Payment.  # noqa: E501

        0 or 1. Indicates if the transaction is secure.  # noqa: E501

        :return: The secure of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """Sets the secure of this InlineResponse20014Payment.

        0 or 1. Indicates if the transaction is secure.  # noqa: E501

        :param secure: The secure of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._secure = secure

    @property
    def split_id(self):
        """Gets the split_id of this InlineResponse20014Payment.  # noqa: E501

        Split identifier in some operations  # noqa: E501

        :return: The split_id of this InlineResponse20014Payment.  # noqa: E501
        :rtype: int
        """
        return self._split_id

    @split_id.setter
    def split_id(self, split_id):
        """Sets the split_id of this InlineResponse20014Payment.

        Split identifier in some operations  # noqa: E501

        :param split_id: The split_id of this InlineResponse20014Payment.  # noqa: E501
        :type: int
        """

        self._split_id = split_id

    @property
    def issuer_bank(self):
        """Gets the issuer_bank of this InlineResponse20014Payment.  # noqa: E501

        Bank of the card  # noqa: E501

        :return: The issuer_bank of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._issuer_bank

    @issuer_bank.setter
    def issuer_bank(self, issuer_bank):
        """Sets the issuer_bank of this InlineResponse20014Payment.

        Bank of the card  # noqa: E501

        :param issuer_bank: The issuer_bank of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._issuer_bank = issuer_bank

    @property
    def auth_code(self):
        """Gets the auth_code of this InlineResponse20014Payment.  # noqa: E501

        Authorization bank code of the transaction (required to execute a return).  # noqa: E501

        :return: The auth_code of this InlineResponse20014Payment.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this InlineResponse20014Payment.

        Authorization bank code of the transaction (required to execute a return).  # noqa: E501

        :param auth_code: The auth_code of this InlineResponse20014Payment.  # noqa: E501
        :type: str
        """

        self._auth_code = auth_code

    @property
    def history(self):
        """Gets the history of this InlineResponse20014Payment.  # noqa: E501


        :return: The history of this InlineResponse20014Payment.  # noqa: E501
        :rtype: list[InlineResponse20014PaymentHistory]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this InlineResponse20014Payment.


        :param history: The history of this InlineResponse20014Payment.  # noqa: E501
        :type: list[InlineResponse20014PaymentHistory]
        """

        self._history = history

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
        if issubclass(InlineResponse20014Payment, dict):
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
        if not isinstance(other, InlineResponse20014Payment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other