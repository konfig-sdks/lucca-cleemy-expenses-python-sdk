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
from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_processed_amounts_vat_bases import ExpenseTempItemProcessedAmountsVatBases

class ExpenseTempItemProcessedAmounts(BaseModel):
    # Original transaction amount converted into the establishment's currency.
    gross_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossAmount')

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currency_id: typing.Optional[str] = Field(None, alias='currencyId')

    currency: typing.Optional[Currency] = Field(None, alias='currency')

    # The converted amount after the expense policy has been applied.
    net_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='netAmount')

    vat_bases: typing.Optional[ExpenseTempItemProcessedAmountsVatBases] = Field(None, alias='vatBases')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
