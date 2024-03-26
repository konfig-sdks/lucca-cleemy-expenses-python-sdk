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


class RequiredExpenseClaimAuthorizedActions(TypedDict):
    pass

class OptionalExpenseClaimAuthorizedActions(TypedDict, total=False):
    # The expenseClaim can be deleted by the current authenticated user.
    isCancellable: bool

    # The expenseClaim can be edited by the current authenticated user.
    isEditable: bool

    # The expenseClaim can be approved by the current authenticated user.
    isApprovable: bool

    # The expenseClaim can be controlled by the current authenticated user.
    isControllable: bool

    # The current authenticated user can cancel the control of the expenseClaim.
    isUnControllable: bool

class ExpenseClaimAuthorizedActions(RequiredExpenseClaimAuthorizedActions, OptionalExpenseClaimAuthorizedActions):
    pass
