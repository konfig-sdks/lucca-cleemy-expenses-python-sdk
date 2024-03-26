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

from lucca_cleemy_expenses_python_sdk.pydantic.expense_temp_item_processed_amounts_vat_bases_item import ExpenseTempItemProcessedAmountsVatBasesItem

ExpenseTempItemProcessedAmountsVatBases = typing.List[ExpenseTempItemProcessedAmountsVatBasesItem]
