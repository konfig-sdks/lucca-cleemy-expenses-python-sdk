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


class RequiredCurrency(TypedDict):
    pass

class OptionalCurrency(TypedDict, total=False):
    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    id: str

    # Label of the currency (eg: Pound sterling).
    name: str

    url: str

class Currency(RequiredCurrency, OptionalCurrency):
    pass
