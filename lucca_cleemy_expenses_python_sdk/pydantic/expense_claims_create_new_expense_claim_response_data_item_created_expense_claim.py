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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lucca_cleemy_expenses_python_sdk.pydantic.expense_claims_create_new_expense_claim_response_data_item_created_expense_claim_next_approver import ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaimNextApprover

class ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    next_approver: typing.Optional[ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaimNextApprover] = Field(None, alias='nextApprover')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
