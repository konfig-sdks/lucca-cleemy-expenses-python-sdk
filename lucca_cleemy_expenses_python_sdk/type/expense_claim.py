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

from lucca_cleemy_expenses_python_sdk.type.approval_state_id import ApprovalStateId
from lucca_cleemy_expenses_python_sdk.type.claim_status_id import ClaimStatusId
from lucca_cleemy_expenses_python_sdk.type.currency import Currency
from lucca_cleemy_expenses_python_sdk.type.entity_base import EntityBase
from lucca_cleemy_expenses_python_sdk.type.enum import Enum
from lucca_cleemy_expenses_python_sdk.type.expense_claim_authorized_actions import ExpenseClaimAuthorizedActions
from lucca_cleemy_expenses_python_sdk.type.owner import Owner
from lucca_cleemy_expenses_python_sdk.type.payment_method_id import PaymentMethodId
from lucca_cleemy_expenses_python_sdk.type.source_id import SourceId

class RequiredExpenseClaim(TypedDict):
    # Day the expenseClaim has been declared (Time zone Europe/Paris).
    declaredOn: datetime

    # Day the expenseClaim has been created (Time zone Europe/Paris).
    createdOn: datetime

    # Day the expenseClaim has been modified (Time zone Europe/Paris).
    modifiedOn: datetime

class OptionalExpenseClaim(TypedDict, total=False):
    id: int

    # Name of the expense claim. If empty, it will be generated with the month and year of the last of claim item.
    name: str

    # Day the expenseClaim has been paid (Time zone Europe/Paris).
    paymentReceivedOn: datetime

    sourceId: SourceId

    source: Enum

    paymentMethodId: PaymentMethodId

    paymentMethod: Enum

    statusId: ClaimStatusId

    status: Enum

    approvalStateId: ApprovalStateId

    approvalState: Enum

    authorizedActions: ExpenseClaimAuthorizedActions

    # Unique identifier of the user that made this expenseClaim.
    ownerId: int

    owner: Owner

    # Unique identifier of the user that created this grouping of expense.
    authorId: int

    author: EntityBase

    legalEntityId: int

    legalEntity: EntityBase

    departmentId: int

    department: EntityBase

    # ISO code of the currency (eg: 'EUR', 'USD', 'GBP', ...).
    currencyId: str

    currency: Currency

class ExpenseClaim(RequiredExpenseClaim, OptionalExpenseClaim):
    pass
