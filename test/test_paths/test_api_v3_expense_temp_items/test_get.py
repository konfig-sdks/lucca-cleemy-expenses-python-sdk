# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest
from unittest.mock import patch

import urllib3

import lucca_cleemy_expenses_python_sdk
from lucca_cleemy_expenses_python_sdk.paths.api_v3_expense_temp_items import get
from lucca_cleemy_expenses_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3ExpenseTempItems(ApiTestMixin, unittest.TestCase):
    """
    ApiV3ExpenseTempItems unit test stubs
        List ExpenseTempItems (temporary expense)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
