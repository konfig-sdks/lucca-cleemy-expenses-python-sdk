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

from lucca_cleemy_expenses_python_sdk.type.expense_claims_create_new_expense_claim_response_data_item_created_expense_claim_next_approver import ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaimNextApprover

class RequiredExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim(TypedDict):
    pass

class OptionalExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim(TypedDict, total=False):
    id: int

    nextApprover: ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaimNextApprover

class ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim(RequiredExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim, OptionalExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim):
    pass
