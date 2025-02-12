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


class ExpenseClaimAuthorizedActions(BaseModel):
    # The expenseClaim can be deleted by the current authenticated user.
    is_cancellable: typing.Optional[bool] = Field(None, alias='isCancellable')

    # The expenseClaim can be edited by the current authenticated user.
    is_editable: typing.Optional[bool] = Field(None, alias='isEditable')

    # The expenseClaim can be approved by the current authenticated user.
    is_approvable: typing.Optional[bool] = Field(None, alias='isApprovable')

    # The expenseClaim can be controlled by the current authenticated user.
    is_controllable: typing.Optional[bool] = Field(None, alias='isControllable')

    # The current authenticated user can cancel the control of the expenseClaim.
    is_un_controllable: typing.Optional[bool] = Field(None, alias='isUnControllable')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
