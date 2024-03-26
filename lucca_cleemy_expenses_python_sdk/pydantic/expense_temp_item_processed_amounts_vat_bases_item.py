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

from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_processed_amounts_vat_bases_item_country_vat_rate import ExpenseTempItemProcessedAmountsVatBasesItemCountryVatRate

class ExpenseTempItemProcessedAmountsVatBasesItem(BaseModel):
    country_vat_rate_id: typing.Optional[int] = Field(None, alias='countryVatRateId')

    country_vat_rate: typing.Optional[ExpenseTempItemProcessedAmountsVatBasesItemCountryVatRate] = Field(None, alias='countryVatRate')

    vat_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='vatAmount')

    amount_excluding_vat: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountExcludingVat')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
