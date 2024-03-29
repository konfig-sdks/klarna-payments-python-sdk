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

from klarna_payments_python_sdk.type.product_identifiers import ProductIdentifiers
from klarna_payments_python_sdk.type.subscription import Subscription

class RequiredOrderLine(TypedDict):
    # Descriptive name of the order line item.
    name: str

    # Quantity of the order line item. Must be a non-negative number.
    quantity: int

    # Total amount of the order line. Must be defined as minor units. Includes tax and discount. Eg: 2000=20 euros Value = (quantity x unit_price) - total_discount_amount.  (max value: 200000000)
    total_amount: int

    # Price for a single unit of the order line. Must be defined as minor units. Includes tax, excludes discount. (max value: 200000000)
    unit_price: int

class OptionalOrderLine(TypedDict, total=False):
    # URL to an image that can be later embedded in communications between Klarna and the customer. (max 1024 characters).  A minimum of 250x250 px resolution is recommended for the image to look good in the Klarna app, and below 50x50 px won't even show. We recommend using a good sized image (650x650 px or more), however the file size must not exceed 12MB.
    image_url: str

    # Used for storing merchant's internal order number or other reference. Pass through field. (max 1024 characters)
    merchant_data: str

    product_identifiers: ProductIdentifiers

    # URL to the product in the merchant’s webshop that can be later used in communications between Klarna and the customer. (max 1024 characters)
    product_url: str

    # Unit used to describe the quantity, e.g. kg, pcs, etc. If defined the value has to be 1-8 characters.
    quantity_unit: str

    # Client facing article number, SKU or similar. Max length is 256 characters.
    reference: str

    # Tax rate of the order line. Non-negative value. The percentage value is represented with two implicit decimals. I.e 2000 = 20%.
    tax_rate: int

    # Non-negative minor units. Includes tax. Eg: 500=5 euros
    total_discount_amount: int

    # Total tax amount of the order line. Must be within ±1 of total_amount - total_amount 10000 / (10000 + tax_rate). Negative when type is discount.
    total_tax_amount: int

    # Type of the order line item. The possible values are:  physical discount shipping_fee sales_tax digital gift_card store_credit surcharge
    type: str

    subscription: Subscription

class OrderLine(RequiredOrderLine, OptionalOrderLine):
    pass
