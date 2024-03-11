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


class Address(BaseModel):
    # Customer’s Title. Allowed values per country: UK - \"Mr\", \"Ms\" DE - \"Herr\", \"Frau\" AT: \"Herr, \"Frau\" CH: de-CH: \"Herr, \"Frau\" it-CH: \"Sig.\", \"Sig.ra\" fr-CH: \"M\", \"Mme\"  BE: \"Dhr.\", \"Mevr.\" NL: \"Dhr.\", \"Mevr.\"
    title: typing.Optional[str] = Field(None, alias='title')

    # ‘Attn.’ (if applicable). Only applicable for B2B customers.
    attention: typing.Optional[str] = Field(None, alias='attention')

    # Customer’s city.
    city: typing.Optional[str] = Field(None, alias='city')

    # Customer’s country. This value overrides the purchase country if they are different. Should follow the standard of ISO 3166 alpha-2. E.g. GB, US, DE, SE.
    country: typing.Optional[str] = Field(None, alias='country')

    # Customer’s email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # Customers family name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’. More information can be found [in this link](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-data-requirements/#details-needed-per-market)
    family_name: typing.Optional[str] = Field(None, alias='family_name')

    # Customers given name in UTF-8 encoding. Cannot be only numbers, must be more than 1 character. Allowed special characters: -'’. More information can be found [in this link](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-data-requirements/#details-needed-per-market)
    given_name: typing.Optional[str] = Field(None, alias='given_name')

    # Organization name (if applicable). Only applicable for B2B customers.
    organization_name: typing.Optional[str] = Field(None, alias='organization_name')

    # Phone number. Preferably a mobile phone number.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # Customer’s postal code. Validation according to Universal Postal Union addressing systems. E.g. 12345, W1G OPW.
    postal_code: typing.Optional[str] = Field(None, alias='postal_code')

    # Customer’s region or state - Mandatory for US and AU market. Validations according to ISO 3166-2 format, e.g. OH, NJ, etc.
    region: typing.Optional[str] = Field(None, alias='region')

    # Customer’s street address. Regional formatting is required, as follows: UK/US/FR: 33 Cavendish Square Rest of EU: De Ruijterkade 7
    street_address: typing.Optional[str] = Field(None, alias='street_address')

    # Customer’s street address. Second Line. 
    street_address2: typing.Optional[str] = Field(None, alias='street_address2')
    class Config:
        arbitrary_types_allowed = True