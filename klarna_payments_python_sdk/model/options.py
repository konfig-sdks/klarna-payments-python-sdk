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


class Options(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class color_border(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^#[A-Fa-f0-9]{6}$',
                    }]
            
            
            class color_border_selected(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^#[A-Fa-f0-9]{6}$',
                    }]
            
            
            class color_details(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^#[A-Fa-f0-9]{6}$',
                    }]
            
            
            class color_text(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^#[A-Fa-f0-9]{6}$',
                    }]
            radius_border = schemas.StrSchema
            __annotations__ = {
                "color_border": color_border,
                "color_border_selected": color_border_selected,
                "color_details": color_details,
                "color_text": color_text,
                "radius_border": radius_border,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_border"]) -> MetaOapg.properties.color_border: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_border_selected"]) -> MetaOapg.properties.color_border_selected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_details"]) -> MetaOapg.properties.color_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color_text"]) -> MetaOapg.properties.color_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radius_border"]) -> MetaOapg.properties.radius_border: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["color_border", "color_border_selected", "color_details", "color_text", "radius_border", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_border"]) -> typing.Union[MetaOapg.properties.color_border, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_border_selected"]) -> typing.Union[MetaOapg.properties.color_border_selected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_details"]) -> typing.Union[MetaOapg.properties.color_details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color_text"]) -> typing.Union[MetaOapg.properties.color_text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radius_border"]) -> typing.Union[MetaOapg.properties.radius_border, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["color_border", "color_border_selected", "color_details", "color_text", "radius_border", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        color_border: typing.Union[MetaOapg.properties.color_border, str, schemas.Unset] = schemas.unset,
        color_border_selected: typing.Union[MetaOapg.properties.color_border_selected, str, schemas.Unset] = schemas.unset,
        color_details: typing.Union[MetaOapg.properties.color_details, str, schemas.Unset] = schemas.unset,
        color_text: typing.Union[MetaOapg.properties.color_text, str, schemas.Unset] = schemas.unset,
        radius_border: typing.Union[MetaOapg.properties.radius_border, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Options':
        return super().__new__(
            cls,
            *args,
            color_border=color_border,
            color_border_selected=color_border_selected,
            color_details=color_details,
            color_text=color_text,
            radius_border=radius_border,
            _configuration=_configuration,
            **kwargs,
        )
