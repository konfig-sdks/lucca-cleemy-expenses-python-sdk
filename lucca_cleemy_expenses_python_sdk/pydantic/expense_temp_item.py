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

from lucca_cleemy_expenses_python_sdk.pydantic.enum import Enum
from lucca_cleemy_expenses_python_sdk.pydantic.expense_receipt import ExpenseReceipt
from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_authorized_actions import ExpenseTempItemAuthorizedActions
from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_original_transaction import ExpenseTempItemOriginalTransaction
from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_processed_amounts import ExpenseTempItemProcessedAmounts
from lucca_cleemy_expenses_python_sdk.pydantic.payment_method_id import PaymentMethodId
from lucca_cleemy_expenses_python_sdk.pydantic.source_id import SourceId
from lucca_cleemy_expenses_python_sdk.pydantic.status_id import StatusId

class ExpenseTempItem(BaseModel):
    # Day the expense was made.
    purchased_on: datetime = Field(alias='purchasedOn')

    # Nature of the expense: Meals, Train, Taxi, Hotels, Taxi, Mileage... List depends on the app configuration.
    expense_nature_id: int = Field(alias='expenseNatureId')

    id: typing.Optional[int] = Field(None, alias='id')

    original_transaction: typing.Optional[ExpenseTempItemOriginalTransaction] = Field(None, alias='originalTransaction')

    processed_amounts: typing.Optional[ExpenseTempItemProcessedAmounts] = Field(None, alias='processedAmounts')

    # Additional information when the expense type is mileage.
    mileage: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='mileage')

    # The quantity when the expense type is 'Quantity'.
    quantity: typing.Optional[int] = Field(None, alias='quantity')

    # Calculated quantity when the expense type is 'Quantity' or 'Invitations' (number of attendees).
    effective_quantity: typing.Optional[int] = Field(None, alias='effectiveQuantity')

    # Additional information when the expense type is 'Invitation'.
    attendees: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='attendees')

    # Axis sections values.
    axis_sections: typing.Optional[typing.List[object]] = Field(None, alias='axisSections')

    # Values for custom fields.
    custom_fields: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='customFields')

    # Merchant of the expense.
    merchant: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='merchant')

    comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='comment')

    # The original receipt (PDF file, image, ...).
    expense_receipts: typing.Optional[typing.List[ExpenseReceipt]] = Field(None, alias='expenseReceipts')

    authorized_actions: typing.Optional[ExpenseTempItemAuthorizedActions] = Field(None, alias='authorizedActions')

    source_id: typing.Optional[SourceId] = Field(None, alias='sourceId')

    source: typing.Optional[Enum] = Field(None, alias='source')

    # Unique identifier of the user that made this expense.
    owner_id: typing.Optional[int] = Field(None, alias='ownerId')

    payment_method_id: typing.Optional[PaymentMethodId] = Field(None, alias='paymentMethodId')

    payment_method: typing.Optional[Enum] = Field(None, alias='paymentMethod')

    status_id: typing.Optional[StatusId] = Field(None, alias='statusId')

    status: typing.Optional[Enum] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
