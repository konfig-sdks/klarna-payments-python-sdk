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


class CustomerRead(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            date_of_birth = schemas.StrSchema
            gender = schemas.StrSchema
            
            
            class organization_entity_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LIMITED_COMPANY(cls):
                    return cls("LIMITED_COMPANY")
                
                @schemas.classproperty
                def PUBLIC_LIMITED_COMPANY(cls):
                    return cls("PUBLIC_LIMITED_COMPANY")
                
                @schemas.classproperty
                def ENTREPRENEURIAL_COMPANY(cls):
                    return cls("ENTREPRENEURIAL_COMPANY")
                
                @schemas.classproperty
                def LIMITED_PARTNERSHIP_LIMITED_COMPANY(cls):
                    return cls("LIMITED_PARTNERSHIP_LIMITED_COMPANY")
                
                @schemas.classproperty
                def LIMITED_PARTNERSHIP(cls):
                    return cls("LIMITED_PARTNERSHIP")
                
                @schemas.classproperty
                def GENERAL_PARTNERSHIP(cls):
                    return cls("GENERAL_PARTNERSHIP")
                
                @schemas.classproperty
                def REGISTERED_SOLE_TRADER(cls):
                    return cls("REGISTERED_SOLE_TRADER")
                
                @schemas.classproperty
                def SOLE_TRADER(cls):
                    return cls("SOLE_TRADER")
                
                @schemas.classproperty
                def CIVIL_LAW_PARTNERSHIP(cls):
                    return cls("CIVIL_LAW_PARTNERSHIP")
                
                @schemas.classproperty
                def PUBLIC_INSTITUTION(cls):
                    return cls("PUBLIC_INSTITUTION")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("OTHER")
            organization_registration_id = schemas.StrSchema
            type = schemas.StrSchema
            vat_id = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "date_of_birth": date_of_birth,
                "gender": gender,
                "organization_entity_type": organization_entity_type,
                "organization_registration_id": organization_registration_id,
                "type": type,
                "vat_id": vat_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_entity_type"]) -> MetaOapg.properties.organization_entity_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_registration_id"]) -> MetaOapg.properties.organization_registration_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vat_id"]) -> MetaOapg.properties.vat_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "date_of_birth", "gender", "organization_entity_type", "organization_registration_id", "type", "vat_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth"]) -> typing.Union[MetaOapg.properties.date_of_birth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_entity_type"]) -> typing.Union[MetaOapg.properties.organization_entity_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_registration_id"]) -> typing.Union[MetaOapg.properties.organization_registration_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vat_id"]) -> typing.Union[MetaOapg.properties.vat_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "date_of_birth", "gender", "organization_entity_type", "organization_registration_id", "type", "vat_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        date_of_birth: typing.Union[MetaOapg.properties.date_of_birth, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        organization_entity_type: typing.Union[MetaOapg.properties.organization_entity_type, str, schemas.Unset] = schemas.unset,
        organization_registration_id: typing.Union[MetaOapg.properties.organization_registration_id, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        vat_id: typing.Union[MetaOapg.properties.vat_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerRead':
        return super().__new__(
            cls,
            *args,
            title=title,
            date_of_birth=date_of_birth,
            gender=gender,
            organization_entity_type=organization_entity_type,
            organization_registration_id=organization_registration_id,
            type=type,
            vat_id=vat_id,
            _configuration=_configuration,
            **kwargs,
        )
