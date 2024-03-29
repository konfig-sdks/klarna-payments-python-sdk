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
from pydantic import BaseModel, Field, RootModel


class CustomerRead(BaseModel):
    # Customer’s Title. Allowed values per country: UK - \"Mr\", \"Ms\" DE - \"Herr\", \"Frau\" AT: \"Herr, \"Frau\" CH: de-CH: \"Herr, \"Frau\" it-CH: \"Sig.\", \"Sig.ra\" fr-CH: \"M\", \"Mme\"  BE: \"Dhr.\", \"Mevr.\" NL: \"Dhr.\", \"Mevr.\"
    title: typing.Optional[str] = Field(None, alias='title')

    # Customer’s date of birth. The format is ‘yyyy-mm-dd’
    date_of_birth: typing.Optional[str] = Field(None, alias='date_of_birth')

    # Customer’s gender - ‘male’ or ‘female’
    gender: typing.Optional[str] = Field(None, alias='gender')

    # Organization entity type. Only applicable for B2B customers.
    organization_entity_type: typing.Optional[Literal["LIMITED_COMPANY", "PUBLIC_LIMITED_COMPANY", "ENTREPRENEURIAL_COMPANY", "LIMITED_PARTNERSHIP_LIMITED_COMPANY", "LIMITED_PARTNERSHIP", "GENERAL_PARTNERSHIP", "REGISTERED_SOLE_TRADER", "SOLE_TRADER", "CIVIL_LAW_PARTNERSHIP", "PUBLIC_INSTITUTION", "OTHER"]] = Field(None, alias='organization_entity_type')

    # Organization registration id. Only applicable for B2B customers.
    organization_registration_id: typing.Optional[str] = Field(None, alias='organization_registration_id')

    # Type of customer in the session. If nothing is added, a B2C session will be the default. If it is a b2b-session, you should enter organization to trigger a B2B session.
    type: typing.Optional[str] = Field(None, alias='type')

    # VAT ID. Only applicable for B2B customers.
    vat_id: typing.Optional[str] = Field(None, alias='vat_id')
    class Config:
        arbitrary_types_allowed = True
