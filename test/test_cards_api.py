# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.28.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.cards_api import CardsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCardsApi(unittest.TestCase):
    """CardsApi unit test stubs"""

    def setUp(self):
        self.api = CardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user(self):
        """Test case for add_user

        Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.  # noqa: E501
        """
        pass

    def test_edit_user(self):
        """Test case for edit_user

        Changes the expiry date, cvc2 or both  # noqa: E501
        """
        pass

    def test_info_user(self):
        """Test case for info_user

        Get card info  # noqa: E501
        """
        pass

    def test_physical_add_card(self):
        """Test case for physical_add_card

        Tokenize a card by physical encrypted data  # noqa: E501
        """
        pass

    def test_remove_user(self):
        """Test case for remove_user

        Removes a card  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()