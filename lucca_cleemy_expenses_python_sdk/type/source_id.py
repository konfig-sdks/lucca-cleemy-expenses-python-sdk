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


class RequiredSourceId(TypedDict):
    pass

class OptionalSourceId(TypedDict, total=False):
    id: str

class SourceId(RequiredSourceId, OptionalSourceId):
    pass
