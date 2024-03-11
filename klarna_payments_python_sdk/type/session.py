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
from klarna_payments_python_sdk.type.attachment import Attachment
from klarna_payments_python_sdk.type.customer import Customer
from klarna_payments_python_sdk.type.merchant_urls import MerchantUrls
from klarna_payments_python_sdk.type.options import Options
from klarna_payments_python_sdk.type.order_line import OrderLine
from klarna_payments_python_sdk.type.payment_method_category import PaymentMethodCategory
from klarna_payments_python_sdk.type.session_custom_payment_method_ids import SessionCustomPaymentMethodIds

class RequiredSession(TypedDict):
    pass

class OptionalSession(TypedDict, total=False):
    # The acquiring channel in which the session takes place. Ecommerce is default unless specified. Any other values should be defined in the agreement.
    acquiring_channel: str

    attachment: Attachment

    # Authorization token.
    authorization_token: str

    billing_address: Address

    # Token to be passed to the JS client
    client_token: str

    custom_payment_method_ids: SessionCustomPaymentMethodIds

    customer: Customer

    # Design package to use in the session. This can only by used if a custom design has been implemented for Klarna Payments and agreed upon in the agreement. It might have a financial impact. Delivery manager will provide the value for the parameter.
    design: str

    # Session expiration date
    expires_at: datetime

    # Used to define the language and region of the customer. The locale follows the format of [RFC 1766](https://datatracker.ietf.org/doc/rfc1766/), meaning its value consists of language-country. Read more on **[Supported Locals and Currencies](https://docs.klarna.com/klarna-payments/in-depth-knowledge/puchase-countries-currencies-locales/)**.
    locale: str

    # Pass through field to send any information about the order to be used later for reference while retrieving the order details (max 6000 characters)
    merchant_data: str

    # Used for storing merchant's internal order number or other reference.
    merchant_reference1: str

    # Used for storing merchant's internal order number or other reference. The value is available in the settlement files. (max 255 characters).
    merchant_reference2: str

    merchant_urls: MerchantUrls

    options: Options

    # Total amount of the order including tax and any available discounts. The value should be in non-negative minor units. Eg: 25 Euros should be 2500.
    order_amount: int

    # The array containing list of line items that are part of this order. Maximum of 1000 line items could be processed in a single order.
    order_lines: typing.List[OrderLine]

    # Total tax amount of the order. The value should be in non-negative minor units. Eg: 25 Euros should be 2500.
    order_tax_amount: int

    # Available payment method categories
    payment_method_categories: typing.List[PaymentMethodCategory]

    # The purchase country of the customer. The billing country always overrides purchase country if the values are different. Formatted according to ISO 3166 alpha-2 standard, e.g. GB, SE, DE, US, etc.
    purchase_country: str

    # The purchase currency of the order. Formatted according to ISO 4217 standard, e.g. USD, EUR, SEK, GBP, etc.
    purchase_currency: str

    shipping_address: Address

    # The current status of the session. Possible values: 'complete', 'incomplete' where 'complete' is set when the order has been placed.
    status: str

    # Intent for the session. The field is designed to let partners inform Klarna of the purpose of the customer’s session.
    intent: str

class Session(RequiredSession, OptionalSession):
    pass
