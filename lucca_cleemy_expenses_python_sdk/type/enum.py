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


class RequiredEnum(TypedDict):
    pass

class OptionalEnum(TypedDict, total=False):
    id: typing.Union[int, float]

    name: str

    code: str

class Enum(RequiredEnum, OptionalEnum):
    pass
