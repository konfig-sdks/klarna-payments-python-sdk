# coding: utf-8

"""
    Klarna Payments API V1

    The payments API is used to create a session to offer Klarna's payment methods as part of your checkout. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).  **Note:** Examples provided in this section includes full payloads, including all supported fields , required and optionals. In order to implement a best in class request we recommend you don't include customer details when initiating a payment session. Refer to [Initiate a payment](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/) section for further details.  Read more on [Klarna payments](https://docs.klarna.com/klarna-payments/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from klarna_payments_python_sdk.type.address import Address
from klarna_payments_python_sdk.type.create_order_request_custom_payment_method_ids import CreateOrderRequestCustomPaymentMethodIds
from klarna_payments_python_sdk.type.customer import Customer
from klarna_payments_python_sdk.type.merchant_urls import MerchantUrls
from klarna_payments_python_sdk.type.order_line import OrderLine
from klarna_payments_python_sdk.type.payment_method_category import PaymentMethodCategory

class RequiredCreateOrderRequest(TypedDict):
    # Total amount of the order including tax and any available discounts. The value should be in non-negative minor units. Eg: 25 Euros should be 2500.
    order_amount: int

    # The array containing list of line items that are part of this order. Maximum of 1000 line items could be processed in a single order.
    order_lines: typing.List[OrderLine]

    # The purchase country of the customer. The billing country always overrides purchase country if the values are different. Formatted according to ISO 3166 alpha-2 standard, e.g. GB, SE, DE, US, etc.
    purchase_country: str

    # The purchase currency of the order. Formatted according to ISO 4217 standard, e.g. USD, EUR, SEK, GBP, etc.
    purchase_currency: str

class OptionalCreateOrderRequest(TypedDict, total=False):
    # Authorization token.
    authorization_token: str

    # Allow merchant to trigger auto capturing.
    auto_capture: bool

    billing_address: Address

    custom_payment_method_ids: CreateOrderRequestCustomPaymentMethodIds

    customer: Customer

    # Used to define the language and region of the customer. The locale follows the format of [RFC 1766](https://datatracker.ietf.org/doc/rfc1766/), meaning its value consists of language-country. Read more on **[Supported Locals and Currencies](https://docs.klarna.com/klarna-payments/in-depth-knowledge/puchase-countries-currencies-locales/)**.
    locale: str

    # Pass through field to send any information about the order to be used later for reference while retrieving the order details (max 6000 characters)
    merchant_data: str

    # Used for storing merchant's internal order number or other reference.
    merchant_reference1: str

    # Used for storing merchant's internal order number or other reference. The value is available in the settlement files. (max 255 characters).
    merchant_reference2: str

    merchant_urls: MerchantUrls

    # Total tax amount of the order. The value should be in non-negative minor units. Eg: 25 Euros should be 2500.
    order_tax_amount: int

    # Available payment method categories
    payment_method_categories: typing.List[PaymentMethodCategory]

    shipping_address: Address

    # The current status of the session. Possible values: 'complete', 'incomplete' where 'complete' is set when the order has been placed.
    status: str

class CreateOrderRequest(RequiredCreateOrderRequest, OptionalCreateOrderRequest):
    pass
