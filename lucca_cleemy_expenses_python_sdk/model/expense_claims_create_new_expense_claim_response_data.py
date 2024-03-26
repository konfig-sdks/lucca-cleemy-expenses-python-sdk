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


class ExpenseClaimsCreateNewExpenseClaimResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExpenseClaimsCreateNewExpenseClaimResponseDataItem']:
            return ExpenseClaimsCreateNewExpenseClaimResponseDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ExpenseClaimsCreateNewExpenseClaimResponseDataItem'], typing.List['ExpenseClaimsCreateNewExpenseClaimResponseDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpenseClaimsCreateNewExpenseClaimResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ExpenseClaimsCreateNewExpenseClaimResponseDataItem':
        return super().__getitem__(i)

from lucca_cleemy_expenses_python_sdk.model.expense_claims_create_new_expense_claim_response_data_item import ExpenseClaimsCreateNewExpenseClaimResponseDataItem
