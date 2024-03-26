# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest

import os
from pprint import pprint
from lucca_cleemy_expenses_python_sdk import LuccaCleemyExpenses

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        luccacleemyexpenses = LuccaCleemyExpenses(
        
                        authorization = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(luccacleemyexpenses)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
