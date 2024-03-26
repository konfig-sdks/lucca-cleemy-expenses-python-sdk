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


class RequiredExpenseTempItemAuthorizedActions(TypedDict):
    pass

class OptionalExpenseTempItemAuthorizedActions(TypedDict, total=False):
    # Expense can be deleted by the current authenticated user.
    isCancellable: bool

    # Expense can be edited by the current authenticated user.
    isEditable: bool

class ExpenseTempItemAuthorizedActions(RequiredExpenseTempItemAuthorizedActions, OptionalExpenseTempItemAuthorizedActions):
    pass
