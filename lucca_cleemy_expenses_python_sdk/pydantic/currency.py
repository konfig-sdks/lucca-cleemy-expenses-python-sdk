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


class Currency(BaseModel):
    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    id: typing.Optional[str] = Field(None, alias='id')

    # Label of the currency (eg: Pound sterling).
    name: typing.Optional[str] = Field(None, alias='name')

    url: typing.Optional[str] = Field(None, alias='url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
