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

from lucca_cleemy_expenses_python_sdk.type.expense_claims_create_new_expense_claim_request_item_expense_temp_items import ExpenseClaimsCreateNewExpenseClaimRequestItemExpenseTempItems

class RequiredExpenseClaimsCreateNewExpenseClaimRequestItem(TypedDict):
    # Human readable name for this ExpenseClaim (eg: \"May 2022\").
    title: str

    expenseTempItems: ExpenseClaimsCreateNewExpenseClaimRequestItemExpenseTempItems

class OptionalExpenseClaimsCreateNewExpenseClaimRequestItem(TypedDict, total=False):
    pass

class ExpenseClaimsCreateNewExpenseClaimRequestItem(RequiredExpenseClaimsCreateNewExpenseClaimRequestItem, OptionalExpenseClaimsCreateNewExpenseClaimRequestItem):
    pass
