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

from klarna_payments_python_sdk.type.payment_method_category import PaymentMethodCategory

class RequiredMerchantSession(TypedDict):
    # Client token to be passed to the JS client while initializing the JS SDK in the next step.
    client_token: str

    # ID of the created session. Please use this ID to share with Klarna for identifying any issues during integration.
    session_id: str

class OptionalMerchantSession(TypedDict, total=False):
    # Available payment method categories for this particular session
    payment_method_categories: typing.List[PaymentMethodCategory]

class MerchantSession(RequiredMerchantSession, OptionalMerchantSession):
    pass
