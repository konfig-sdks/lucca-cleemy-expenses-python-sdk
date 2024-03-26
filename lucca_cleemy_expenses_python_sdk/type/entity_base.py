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


class RequiredEntityBase(TypedDict):
    pass

class OptionalEntityBase(TypedDict, total=False):
    id: int

    name: str

    url: str

class EntityBase(RequiredEntityBase, OptionalEntityBase):
    pass
