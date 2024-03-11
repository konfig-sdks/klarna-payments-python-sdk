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


class CreateOrderRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "order_amount",
            "purchase_country",
            "order_lines",
            "purchase_currency",
        }
        
        class properties:
            
            
            class order_amount(
                schemas.Int64Schema
            ):
                pass
            
            
            class order_lines(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OrderLine']:
                        return OrderLine
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OrderLine'], typing.List['OrderLine']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'order_lines':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OrderLine':
                    return super().__getitem__(i)
            
            
            class purchase_country(
                schemas.StrSchema
            ):
                pass
            
            
            class purchase_currency(
                schemas.StrSchema
            ):
                pass
            authorization_token = schemas.StrSchema
            auto_capture = schemas.BoolSchema
        
            @staticmethod
            def billing_address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def custom_payment_method_ids() -> typing.Type['CreateOrderRequestCustomPaymentMethodIds']:
                return CreateOrderRequestCustomPaymentMethodIds
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
            
            
            class locale(
                schemas.StrSchema
            ):
                pass
            
            
            class merchant_data(
                schemas.StrSchema
            ):
                pass
            
            
            class merchant_reference1(
                schemas.StrSchema
            ):
                pass
            
            
            class merchant_reference2(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def merchant_urls() -> typing.Type['MerchantUrls']:
                return MerchantUrls
            
            
            class order_tax_amount(
                schemas.Int64Schema
            ):
                pass
            
            
            class payment_method_categories(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentMethodCategory']:
                        return PaymentMethodCategory
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PaymentMethodCategory'], typing.List['PaymentMethodCategory']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_method_categories':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentMethodCategory':
                    return super().__getitem__(i)
        
            @staticmethod
            def shipping_address() -> typing.Type['Address']:
                return Address
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("complete")
                
                @schemas.classproperty
                def INCOMPLETE(cls):
                    return cls("incomplete")
            __annotations__ = {
                "order_amount": order_amount,
                "order_lines": order_lines,
                "purchase_country": purchase_country,
                "purchase_currency": purchase_currency,
                "authorization_token": authorization_token,
                "auto_capture": auto_capture,
                "billing_address": billing_address,
                "custom_payment_method_ids": custom_payment_method_ids,
                "customer": customer,
                "locale": locale,
                "merchant_data": merchant_data,
                "merchant_reference1": merchant_reference1,
                "merchant_reference2": merchant_reference2,
                "merchant_urls": merchant_urls,
                "order_tax_amount": order_tax_amount,
                "payment_method_categories": payment_method_categories,
                "shipping_address": shipping_address,
                "status": status,
            }
    
    order_amount: MetaOapg.properties.order_amount
    purchase_country: MetaOapg.properties.purchase_country
    order_lines: MetaOapg.properties.order_lines
    purchase_currency: MetaOapg.properties.purchase_currency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_amount"]) -> MetaOapg.properties.order_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_lines"]) -> MetaOapg.properties.order_lines: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_token"]) -> MetaOapg.properties.authorization_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_capture"]) -> MetaOapg.properties.auto_capture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_payment_method_ids"]) -> 'CreateOrderRequestCustomPaymentMethodIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_data"]) -> MetaOapg.properties.merchant_data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_reference1"]) -> MetaOapg.properties.merchant_reference1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_reference2"]) -> MetaOapg.properties.merchant_reference2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_urls"]) -> 'MerchantUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_tax_amount"]) -> MetaOapg.properties.order_tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method_categories"]) -> MetaOapg.properties.payment_method_categories: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["order_amount", "order_lines", "purchase_country", "purchase_currency", "authorization_token", "auto_capture", "billing_address", "custom_payment_method_ids", "customer", "locale", "merchant_data", "merchant_reference1", "merchant_reference2", "merchant_urls", "order_tax_amount", "payment_method_categories", "shipping_address", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_amount"]) -> MetaOapg.properties.order_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_lines"]) -> MetaOapg.properties.order_lines: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_token"]) -> typing.Union[MetaOapg.properties.authorization_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_capture"]) -> typing.Union[MetaOapg.properties.auto_capture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_payment_method_ids"]) -> typing.Union['CreateOrderRequestCustomPaymentMethodIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['Customer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union[MetaOapg.properties.locale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_data"]) -> typing.Union[MetaOapg.properties.merchant_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_reference1"]) -> typing.Union[MetaOapg.properties.merchant_reference1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_reference2"]) -> typing.Union[MetaOapg.properties.merchant_reference2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_urls"]) -> typing.Union['MerchantUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_tax_amount"]) -> typing.Union[MetaOapg.properties.order_tax_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method_categories"]) -> typing.Union[MetaOapg.properties.payment_method_categories, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["order_amount", "order_lines", "purchase_country", "purchase_currency", "authorization_token", "auto_capture", "billing_address", "custom_payment_method_ids", "customer", "locale", "merchant_data", "merchant_reference1", "merchant_reference2", "merchant_urls", "order_tax_amount", "payment_method_categories", "shipping_address", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        order_amount: typing.Union[MetaOapg.properties.order_amount, decimal.Decimal, int, ],
        purchase_country: typing.Union[MetaOapg.properties.purchase_country, str, ],
        order_lines: typing.Union[MetaOapg.properties.order_lines, list, tuple, ],
        purchase_currency: typing.Union[MetaOapg.properties.purchase_currency, str, ],
        authorization_token: typing.Union[MetaOapg.properties.authorization_token, str, schemas.Unset] = schemas.unset,
        auto_capture: typing.Union[MetaOapg.properties.auto_capture, bool, schemas.Unset] = schemas.unset,
        billing_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        custom_payment_method_ids: typing.Union['CreateOrderRequestCustomPaymentMethodIds', schemas.Unset] = schemas.unset,
        customer: typing.Union['Customer', schemas.Unset] = schemas.unset,
        locale: typing.Union[MetaOapg.properties.locale, str, schemas.Unset] = schemas.unset,
        merchant_data: typing.Union[MetaOapg.properties.merchant_data, str, schemas.Unset] = schemas.unset,
        merchant_reference1: typing.Union[MetaOapg.properties.merchant_reference1, str, schemas.Unset] = schemas.unset,
        merchant_reference2: typing.Union[MetaOapg.properties.merchant_reference2, str, schemas.Unset] = schemas.unset,
        merchant_urls: typing.Union['MerchantUrls', schemas.Unset] = schemas.unset,
        order_tax_amount: typing.Union[MetaOapg.properties.order_tax_amount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_method_categories: typing.Union[MetaOapg.properties.payment_method_categories, list, tuple, schemas.Unset] = schemas.unset,
        shipping_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrderRequest':
        return super().__new__(
            cls,
            *args,
            order_amount=order_amount,
            purchase_country=purchase_country,
            order_lines=order_lines,
            purchase_currency=purchase_currency,
            authorization_token=authorization_token,
            auto_capture=auto_capture,
            billing_address=billing_address,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_payments_python_sdk.model.address import Address
from klarna_payments_python_sdk.model.create_order_request_custom_payment_method_ids import CreateOrderRequestCustomPaymentMethodIds
from klarna_payments_python_sdk.model.customer import Customer
from klarna_payments_python_sdk.model.merchant_urls import MerchantUrls
from klarna_payments_python_sdk.model.order_line import OrderLine
from klarna_payments_python_sdk.model.payment_method_category import PaymentMethodCategory
