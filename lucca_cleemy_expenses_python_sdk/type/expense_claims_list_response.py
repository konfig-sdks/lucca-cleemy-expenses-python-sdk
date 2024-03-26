# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lucca_cleemy_expenses_python_sdk.type.expense_claims_list_response_data import ExpenseClaimsListResponseData

class RequiredExpenseClaimsListResponse(TypedDict):
    pass

class OptionalExpenseClaimsListResponse(TypedDict, total=False):
    data: ExpenseClaimsListResponseData

class ExpenseClaimsListResponse(RequiredExpenseClaimsListResponse, OptionalExpenseClaimsListResponse):
    pass
