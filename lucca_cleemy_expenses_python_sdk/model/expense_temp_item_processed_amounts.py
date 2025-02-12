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


class ExpenseTempItemProcessedAmounts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Various amounts in the establishment's currency.
    """


    class MetaOapg:
        
        class properties:
            
            
            class grossAmount(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    multiple_of = 0.01
            currencyId = schemas.StrSchema
        
            @staticmethod
            def currency() -> typing.Type['Currency']:
                return Currency
            
            
            class netAmount(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    multiple_of = 0.01
        
            @staticmethod
            def vatBases() -> typing.Type['ExpenseTempItemProcessedAmountsVatBases']:
                return ExpenseTempItemProcessedAmountsVatBases
            __annotations__ = {
                "grossAmount": grossAmount,
                "currencyId": currencyId,
                "currency": currency,
                "netAmount": netAmount,
                "vatBases": vatBases,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossAmount"]) -> MetaOapg.properties.grossAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyId"]) -> MetaOapg.properties.currencyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netAmount"]) -> MetaOapg.properties.netAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vatBases"]) -> 'ExpenseTempItemProcessedAmountsVatBases': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["grossAmount", "currencyId", "currency", "netAmount", "vatBases", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossAmount"]) -> typing.Union[MetaOapg.properties.grossAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyId"]) -> typing.Union[MetaOapg.properties.currencyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union['Currency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netAmount"]) -> typing.Union[MetaOapg.properties.netAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vatBases"]) -> typing.Union['ExpenseTempItemProcessedAmountsVatBases', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["grossAmount", "currencyId", "currency", "netAmount", "vatBases", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grossAmount: typing.Union[MetaOapg.properties.grossAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currencyId: typing.Union[MetaOapg.properties.currencyId, str, schemas.Unset] = schemas.unset,
        currency: typing.Union['Currency', schemas.Unset] = schemas.unset,
        netAmount: typing.Union[MetaOapg.properties.netAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        vatBases: typing.Union['ExpenseTempItemProcessedAmountsVatBases', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseTempItemProcessedAmounts':
        return super().__new__(
            cls,
            *args,
            grossAmount=grossAmount,
            currencyId=currencyId,
            currency=currency,
            netAmount=netAmount,
            vatBases=vatBases,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_cleemy_expenses_python_sdk.model.currency import Currency
from lucca_cleemy_expenses_python_sdk.model.expense_temp_item_processed_amounts_vat_bases import ExpenseTempItemProcessedAmountsVatBases
