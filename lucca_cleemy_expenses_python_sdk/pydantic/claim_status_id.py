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


class ClaimStatusId(BaseModel):
    id: typing.Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
