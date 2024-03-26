# coding: utf-8
"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import typing
import inspect
from datetime import date, datetime
from lucca_cleemy_expenses_python_sdk.client_custom import ClientCustom
from lucca_cleemy_expenses_python_sdk.configuration import Configuration
from lucca_cleemy_expenses_python_sdk.api_client import ApiClient
from lucca_cleemy_expenses_python_sdk.type_util import copy_signature
from lucca_cleemy_expenses_python_sdk.apis.tags.expense_claims_api import ExpenseClaimsApi
from lucca_cleemy_expenses_python_sdk.apis.tags.expenses_api import ExpensesApi



class LuccaCleemyExpenses(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.expense_claims: ExpenseClaimsApi = ExpenseClaimsApi(api_client)
        self.expenses: ExpensesApi = ExpensesApi(api_client)
