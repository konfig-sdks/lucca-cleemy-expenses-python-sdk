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

from lucca_cleemy_expenses_python_sdk.type.currency import Currency

class RequiredExpenseTempItemOriginalTransaction(TypedDict):
    pass

class OptionalExpenseTempItemOriginalTransaction(TypedDict, total=False):
    grossAmount: typing.Union[int, float]

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currencyId: str

    # Whether the expense was made in a different country than the owner establishment's.
    isExpenseAbroad: bool

    currency: Currency

class ExpenseTempItemOriginalTransaction(RequiredExpenseTempItemOriginalTransaction, OptionalExpenseTempItemOriginalTransaction):
    pass
