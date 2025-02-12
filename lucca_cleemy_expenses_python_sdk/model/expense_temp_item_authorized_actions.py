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


class ExpenseTempItemAuthorizedActions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Authorized actions on the expense for the current user.
    """


    class MetaOapg:
        
        class properties:
            isCancellable = schemas.BoolSchema
            isEditable = schemas.BoolSchema
            __annotations__ = {
                "isCancellable": isCancellable,
                "isEditable": isEditable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isCancellable"]) -> MetaOapg.properties.isCancellable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEditable"]) -> MetaOapg.properties.isEditable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isCancellable", "isEditable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isCancellable"]) -> typing.Union[MetaOapg.properties.isCancellable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEditable"]) -> typing.Union[MetaOapg.properties.isEditable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isCancellable", "isEditable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isCancellable: typing.Union[MetaOapg.properties.isCancellable, bool, schemas.Unset] = schemas.unset,
        isEditable: typing.Union[MetaOapg.properties.isEditable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseTempItemAuthorizedActions':
        return super().__new__(
            cls,
            *args,
            isCancellable=isCancellable,
            isEditable=isEditable,
            _configuration=_configuration,
            **kwargs,
        )
