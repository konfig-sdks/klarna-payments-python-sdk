# coding: utf-8

"""
    Klarna Payments API V1

    The payments API is used to create a session to offer Klarna's payment methods as part of your checkout. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).  **Note:** Examples provided in this section includes full payloads, including all supported fields , required and optionals. In order to implement a best in class request we recommend you don't include customer details when initiating a payment session. Refer to [Initiate a payment](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/) section for further details.  Read more on [Klarna payments](https://docs.klarna.com/klarna-payments/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
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

from klarna_payments_python_sdk import schemas  # noqa: F401


class ProductIdentifiers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class brand(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 70
                    min_length = 0
            
            
            class category_path(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 750
                    min_length = 0
            
            
            class global_trade_item_number(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
                    min_length = 0
            
            
            class manufacturer_part_number(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 70
                    min_length = 0
            
            
            class color(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 0
            
            
            class size(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 0
            __annotations__ = {
                "brand": brand,
                "category_path": category_path,
                "global_trade_item_number": global_trade_item_number,
                "manufacturer_part_number": manufacturer_part_number,
                "color": color,
                "size": size,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand"]) -> MetaOapg.properties.brand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_path"]) -> MetaOapg.properties.category_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["global_trade_item_number"]) -> MetaOapg.properties.global_trade_item_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer_part_number"]) -> MetaOapg.properties.manufacturer_part_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["brand", "category_path", "global_trade_item_number", "manufacturer_part_number", "color", "size", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand"]) -> typing.Union[MetaOapg.properties.brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_path"]) -> typing.Union[MetaOapg.properties.category_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["global_trade_item_number"]) -> typing.Union[MetaOapg.properties.global_trade_item_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer_part_number"]) -> typing.Union[MetaOapg.properties.manufacturer_part_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["brand", "category_path", "global_trade_item_number", "manufacturer_part_number", "color", "size", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        brand: typing.Union[MetaOapg.properties.brand, str, schemas.Unset] = schemas.unset,
        category_path: typing.Union[MetaOapg.properties.category_path, str, schemas.Unset] = schemas.unset,
        global_trade_item_number: typing.Union[MetaOapg.properties.global_trade_item_number, str, schemas.Unset] = schemas.unset,
        manufacturer_part_number: typing.Union[MetaOapg.properties.manufacturer_part_number, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductIdentifiers':
        return super().__new__(
            cls,
            *args,
            brand=brand,
            category_path=category_path,
            global_trade_item_number=global_trade_item_number,
            manufacturer_part_number=manufacturer_part_number,
            color=color,
            size=size,
            _configuration=_configuration,
            **kwargs,
        )