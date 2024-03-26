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

from lucca_cleemy_expenses_python_sdk.pydantic.approval_state_id import ApprovalStateId
from lucca_cleemy_expenses_python_sdk.pydantic.claim_status_id import ClaimStatusId
from lucca_cleemy_expenses_python_sdk.pydantic.currency import Currency
from lucca_cleemy_expenses_python_sdk.pydantic.entity_base import EntityBase
from lucca_cleemy_expenses_python_sdk.pydantic.enum import Enum
from lucca_cleemy_expenses_python_sdk.pydantic.expense_claim_authorized_actions import ExpenseClaimAuthorizedActions
from lucca_cleemy_expenses_python_sdk.pydantic.owner import Owner
from lucca_cleemy_expenses_python_sdk.pydantic.payment_method_id import PaymentMethodId
from lucca_cleemy_expenses_python_sdk.pydantic.source_id import SourceId

class ExpenseClaim(BaseModel):
    # Day the expenseClaim has been declared (Time zone Europe/Paris).
    declared_on: datetime = Field(alias='declaredOn')

    # Day the expenseClaim has been created (Time zone Europe/Paris).
    created_on: datetime = Field(alias='createdOn')

    # Day the expenseClaim has been modified (Time zone Europe/Paris).
    modified_on: datetime = Field(alias='modifiedOn')

    id: typing.Optional[int] = Field(None, alias='id')

    # Name of the expense claim. If empty, it will be generated with the month and year of the last of claim item.
    name: typing.Optional[str] = Field(None, alias='name')

    # Day the expenseClaim has been paid (Time zone Europe/Paris).
    payment_received_on: typing.Optional[datetime] = Field(None, alias='paymentReceivedOn')

    source_id: typing.Optional[SourceId] = Field(None, alias='sourceId')

    source: typing.Optional[Enum] = Field(None, alias='source')

    payment_method_id: typing.Optional[PaymentMethodId] = Field(None, alias='paymentMethodId')

    payment_method: typing.Optional[Enum] = Field(None, alias='paymentMethod')

    status_id: typing.Optional[ClaimStatusId] = Field(None, alias='statusId')

    status: typing.Optional[Enum] = Field(None, alias='status')

    approval_state_id: typing.Optional[ApprovalStateId] = Field(None, alias='approvalStateId')

    approval_state: typing.Optional[Enum] = Field(None, alias='approvalState')

    authorized_actions: typing.Optional[ExpenseClaimAuthorizedActions] = Field(None, alias='authorizedActions')

    # Unique identifier of the user that made this expenseClaim.
    owner_id: typing.Optional[int] = Field(None, alias='ownerId')

    owner: typing.Optional[Owner] = Field(None, alias='owner')

    # Unique identifier of the user that created this grouping of expense.
    author_id: typing.Optional[int] = Field(None, alias='authorId')

    author: typing.Optional[EntityBase] = Field(None, alias='author')

    legal_entity_id: typing.Optional[int] = Field(None, alias='legalEntityId')

    legal_entity: typing.Optional[EntityBase] = Field(None, alias='legalEntity')

    department_id: typing.Optional[int] = Field(None, alias='departmentId')

    department: typing.Optional[EntityBase] = Field(None, alias='department')

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currency_id: typing.Optional[str] = Field(None, alias='currencyId')

    currency: typing.Optional[Currency] = Field(None, alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
