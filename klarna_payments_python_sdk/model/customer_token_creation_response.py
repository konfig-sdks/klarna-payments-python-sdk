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


class CustomerTokenCreationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "token_id",
        }
        
        class properties:
            token_id = schemas.StrSchema
        
            @staticmethod
            def billing_address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def customer() -> typing.Type['CustomerReadCreateToken']:
                return CustomerReadCreateToken
            payment_method_reference = schemas.StrSchema
            redirect_url = schemas.StrSchema
            __annotations__ = {
                "token_id": token_id,
                "billing_address": billing_address,
                "customer": customer,
                "payment_method_reference": payment_method_reference,
                "redirect_url": redirect_url,
            }
    
    token_id: MetaOapg.properties.token_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'CustomerReadCreateToken': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method_reference"]) -> MetaOapg.properties.payment_method_reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_id", "billing_address", "customer", "payment_method_reference", "redirect_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_id"]) -> MetaOapg.properties.token_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['CustomerReadCreateToken', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method_reference"]) -> typing.Union[MetaOapg.properties.payment_method_reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_id", "billing_address", "customer", "payment_method_reference", "redirect_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        token_id: typing.Union[MetaOapg.properties.token_id, str, ],
        billing_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        customer: typing.Union['CustomerReadCreateToken', schemas.Unset] = schemas.unset,
        payment_method_reference: typing.Union[MetaOapg.properties.payment_method_reference, str, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerTokenCreationResponse':
        return super().__new__(
            cls,
            *args,
            token_id=token_id,
            billing_address=billing_address,
            customer=customer,
            payment_method_reference=payment_method_reference,
            redirect_url=redirect_url,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_payments_python_sdk.model.address import Address
from klarna_payments_python_sdk.model.customer_read_create_token import CustomerReadCreateToken
