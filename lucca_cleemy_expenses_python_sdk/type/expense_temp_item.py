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

from lucca_cleemy_expenses_python_sdk.type.enum import Enum
from lucca_cleemy_expenses_python_sdk.type.expense_receipt import ExpenseReceipt
from lucca_cleemy_expenses_python_sdk.type.expense_temp_item_authorized_actions import ExpenseTempItemAuthorizedActions
from lucca_cleemy_expenses_python_sdk.type.expense_temp_item_original_transaction import ExpenseTempItemOriginalTransaction
from lucca_cleemy_expenses_python_sdk.type.expense_temp_item_processed_amounts import ExpenseTempItemProcessedAmounts
from lucca_cleemy_expenses_python_sdk.type.payment_method_id import PaymentMethodId
from lucca_cleemy_expenses_python_sdk.type.source_id import SourceId
from lucca_cleemy_expenses_python_sdk.type.status_id import StatusId

class RequiredExpenseTempItem(TypedDict):
    # Day the expense was made.
    purchasedOn: datetime

    # Nature of the expense: Meals, Train, Taxi, Hotels, Taxi, Mileage... List depends on the app configuration.
    expenseNatureId: int

class OptionalExpenseTempItem(TypedDict, total=False):
    id: int

    originalTransaction: ExpenseTempItemOriginalTransaction

    processedAmounts: ExpenseTempItemProcessedAmounts

    # Additional information when the expense type is mileage.
    mileage: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The quantity when the expense type is 'Quantity'.
    quantity: int

    # Calculated quantity when the expense type is 'Quantity' or 'Invitations' (number of attendees).
    effectiveQuantity: int

    # Additional information when the expense type is 'Invitation'.
    attendees: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Axis sections values.
    axisSections: typing.List[object]

    # Values for custom fields.
    customFields: typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # Merchant of the expense.
    merchant: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    comment: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The original receipt (PDF file, image, ...).
    expenseReceipts: typing.List[ExpenseReceipt]

    authorizedActions: ExpenseTempItemAuthorizedActions

    sourceId: SourceId

    source: Enum

    # Unique identifier of the user that made this expense.
    ownerId: int

    paymentMethodId: PaymentMethodId

    paymentMethod: Enum

    statusId: StatusId

    status: Enum

class ExpenseTempItem(RequiredExpenseTempItem, OptionalExpenseTempItem):
    pass
