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

from lucca_cleemy_expenses_python_sdk.pydantic.currency import Currency

class ExpenseTempItemOriginalTransaction(BaseModel):
    gross_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossAmount')

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currency_id: typing.Optional[str] = Field(None, alias='currencyId')

    # Whether the expense was made in a different country than the owner establishment's.
    is_expense_abroad: typing.Optional[bool] = Field(None, alias='isExpenseAbroad')

    currency: typing.Optional[Currency] = Field(None, alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
