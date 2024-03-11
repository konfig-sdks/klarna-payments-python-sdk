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


class CustomerTokenCreationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "intended_use",
            "purchase_country",
            "purchase_currency",
            "description",
            "locale",
        }
        
        class properties:
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
            class intended_use(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SUBSCRIPTION": "SUBSCRIPTION",
                    }
                
                @schemas.classproperty
                def SUBSCRIPTION(cls):
                    return cls("SUBSCRIPTION")
            
            
            class locale(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[A-Za-z]{2,2}(?:-[A-Za-z]{2,2})*$',
                    }]
            
            
            class purchase_country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[A-Za-z]{2,2}$',
                    }]
            
            
            class purchase_currency(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[A-Za-z]{3,3}$',
                    }]
        
            @staticmethod
            def billing_address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
            __annotations__ = {
                "description": description,
                "intended_use": intended_use,
                "locale": locale,
                "purchase_country": purchase_country,
                "purchase_currency": purchase_currency,
                "billing_address": billing_address,
                "customer": customer,
            }
    
    intended_use: MetaOapg.properties.intended_use
    purchase_country: MetaOapg.properties.purchase_country
    purchase_currency: MetaOapg.properties.purchase_currency
    description: MetaOapg.properties.description
    locale: MetaOapg.properties.locale
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intended_use"]) -> MetaOapg.properties.intended_use: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "intended_use", "locale", "purchase_country", "purchase_currency", "billing_address", "customer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intended_use"]) -> MetaOapg.properties.intended_use: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['Customer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "intended_use", "locale", "purchase_country", "purchase_currency", "billing_address", "customer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        intended_use: typing.Union[MetaOapg.properties.intended_use, str, ],
        purchase_country: typing.Union[MetaOapg.properties.purchase_country, str, ],
        purchase_currency: typing.Union[MetaOapg.properties.purchase_currency, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        locale: typing.Union[MetaOapg.properties.locale, str, ],
        billing_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        customer: typing.Union['Customer', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerTokenCreationRequest':
        return super().__new__(
            cls,
            *args,
            intended_use=intended_use,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            description=description,
            locale=locale,
            billing_address=billing_address,
            customer=customer,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_payments_python_sdk.model.address import Address
from klarna_payments_python_sdk.model.customer import Customer
