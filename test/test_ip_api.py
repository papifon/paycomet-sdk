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
from swagger_client.api.ip_api import IpApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIpApi(unittest.TestCase):
    """IpApi unit test stubs"""

    def setUp(self):
        self.api = IpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_countryby_ip(self):
        """Test case for get_countryby_ip

        Retrieves country info by IP  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()