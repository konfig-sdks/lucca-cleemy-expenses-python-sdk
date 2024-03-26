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
from lucca_cleemy_expenses_python_sdk.type.expense_temp_item_processed_amounts_vat_bases import ExpenseTempItemProcessedAmountsVatBases

class RequiredExpenseTempItemProcessedAmounts(TypedDict):
    pass

class OptionalExpenseTempItemProcessedAmounts(TypedDict, total=False):
    # Original transaction amount converted into the establishment's currency.
    grossAmount: typing.Union[int, float]

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currencyId: str

    currency: Currency

    # The converted amount after the expense policy has been applied.
    netAmount: typing.Union[int, float]

    vatBases: ExpenseTempItemProcessedAmountsVatBases

class ExpenseTempItemProcessedAmounts(RequiredExpenseTempItemProcessedAmounts, OptionalExpenseTempItemProcessedAmounts):
    pass
