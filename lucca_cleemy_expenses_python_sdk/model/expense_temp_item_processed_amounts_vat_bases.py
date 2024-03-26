# coding: utf-8

"""
    Cleemy Expenses

    Welcome on the documentation for the CleemyExpenses API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_cleemy_expenses_python_sdk import schemas  # noqa: F401


class ExpenseTempItemProcessedAmountsVatBases(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExpenseTempItemProcessedAmountsVatBasesItem']:
            return ExpenseTempItemProcessedAmountsVatBasesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ExpenseTempItemProcessedAmountsVatBasesItem'], typing.List['ExpenseTempItemProcessedAmountsVatBasesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpenseTempItemProcessedAmountsVatBases':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ExpenseTempItemProcessedAmountsVatBasesItem':
        return super().__getitem__(i)

from lucca_cleemy_expenses_python_sdk.model.expense_temp_item_processed_amounts_vat_bases_item import ExpenseTempItemProcessedAmountsVatBasesItem
