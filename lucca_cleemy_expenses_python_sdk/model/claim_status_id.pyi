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


class ClaimStatusId(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Status of the expenseClaim.
- 1: the expenseClaim is created.
- 2: the expenseClaim has been partially approved.
- 3: the expenseClaim has been approved.
- 4: the expenseClaim has been controlled.
- 5: the expenseClaim has been approved and controlled.
- 6: the payment of the expenseClaim has been initiated.
- 7: the expenseClaim has been paid.
- 8: the expenseClaim has been refused.
- 9: the expenseClaim has been cancelled.
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.EnumBase,
                schemas.NumberSchema
            ):
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls(6)
                
                @schemas.classproperty
                def POSITIVE_7(cls):
                    return cls(7)
                
                @schemas.classproperty
                def POSITIVE_8(cls):
                    return cls(8)
            __annotations__ = {
                "id": id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClaimStatusId':
        return super().__new__(
            cls,
            *args,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
