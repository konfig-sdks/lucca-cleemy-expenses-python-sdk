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


class ExpenseClaimsCreateNewExpenseClaimResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def createdExpenseClaim() -> typing.Type['ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim']:
                return ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim
            __annotations__ = {
                "createdExpenseClaim": createdExpenseClaim,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdExpenseClaim"]) -> 'ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["createdExpenseClaim", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdExpenseClaim"]) -> typing.Union['ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["createdExpenseClaim", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdExpenseClaim: typing.Union['ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseClaimsCreateNewExpenseClaimResponseDataItem':
        return super().__new__(
            cls,
            *args,
            createdExpenseClaim=createdExpenseClaim,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_cleemy_expenses_python_sdk.model.expense_claims_create_new_expense_claim_response_data_item_created_expense_claim import ExpenseClaimsCreateNewExpenseClaimResponseDataItemCreatedExpenseClaim
