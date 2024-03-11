# coding: utf-8

"""
    Klarna Payments API V1

    The payments API is used to create a session to offer Klarna's payment methods as part of your checkout. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).  **Note:** Examples provided in this section includes full payloads, including all supported fields , required and optionals. In order to implement a best in class request we recommend you don't include customer details when initiating a payment session. Refer to [Initiate a payment](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/) section for further details.  Read more on [Klarna payments](https://docs.klarna.com/klarna-payments/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from klarna_payments_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from klarna_payments_python_sdk.api_response import AsyncGeneratorResponse
from klarna_payments_python_sdk import api_client, exceptions
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

from klarna_payments_python_sdk.model.merchant_urls import MerchantUrls as MerchantUrlsSchema
from klarna_payments_python_sdk.model.payment_method_category import PaymentMethodCategory as PaymentMethodCategorySchema
from klarna_payments_python_sdk.model.session_create_custom_payment_method_ids import SessionCreateCustomPaymentMethodIds as SessionCreateCustomPaymentMethodIdsSchema
from klarna_payments_python_sdk.model.merchant_session import MerchantSession as MerchantSessionSchema
from klarna_payments_python_sdk.model.customer import Customer as CustomerSchema
from klarna_payments_python_sdk.model.attachment import Attachment as AttachmentSchema
from klarna_payments_python_sdk.model.session_create import SessionCreate as SessionCreateSchema
from klarna_payments_python_sdk.model.order_line import OrderLine as OrderLineSchema
from klarna_payments_python_sdk.model.address import Address as AddressSchema
from klarna_payments_python_sdk.model.options import Options as OptionsSchema

from klarna_payments_python_sdk.type.merchant_session import MerchantSession
from klarna_payments_python_sdk.type.payment_method_category import PaymentMethodCategory
from klarna_payments_python_sdk.type.session_create import SessionCreate
from klarna_payments_python_sdk.type.options import Options
from klarna_payments_python_sdk.type.merchant_urls import MerchantUrls
from klarna_payments_python_sdk.type.attachment import Attachment
from klarna_payments_python_sdk.type.address import Address
from klarna_payments_python_sdk.type.order_line import OrderLine
from klarna_payments_python_sdk.type.customer import Customer
from klarna_payments_python_sdk.type.session_create_custom_payment_method_ids import SessionCreateCustomPaymentMethodIds

from ...api_client import Dictionary
from klarna_payments_python_sdk.pydantic.address import Address as AddressPydantic
from klarna_payments_python_sdk.pydantic.options import Options as OptionsPydantic
from klarna_payments_python_sdk.pydantic.session_create_custom_payment_method_ids import SessionCreateCustomPaymentMethodIds as SessionCreateCustomPaymentMethodIdsPydantic
from klarna_payments_python_sdk.pydantic.attachment import Attachment as AttachmentPydantic
from klarna_payments_python_sdk.pydantic.merchant_session import MerchantSession as MerchantSessionPydantic
from klarna_payments_python_sdk.pydantic.merchant_urls import MerchantUrls as MerchantUrlsPydantic
from klarna_payments_python_sdk.pydantic.order_line import OrderLine as OrderLinePydantic
from klarna_payments_python_sdk.pydantic.customer import Customer as CustomerPydantic
from klarna_payments_python_sdk.pydantic.payment_method_category import PaymentMethodCategory as PaymentMethodCategoryPydantic
from klarna_payments_python_sdk.pydantic.session_create import SessionCreate as SessionCreatePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SessionCreateSchema


request_body_session_create = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = MerchantSessionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MerchantSession


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MerchantSession


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_session_mapped_args(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if acquiring_channel is not None:
            _body["acquiring_channel"] = acquiring_channel
        if attachment is not None:
            _body["attachment"] = attachment
        if authorization_token is not None:
            _body["authorization_token"] = authorization_token
        if billing_address is not None:
            _body["billing_address"] = billing_address
        if client_token is not None:
            _body["client_token"] = client_token
        if custom_payment_method_ids is not None:
            _body["custom_payment_method_ids"] = custom_payment_method_ids
        if customer is not None:
            _body["customer"] = customer
        if design is not None:
            _body["design"] = design
        if expires_at is not None:
            _body["expires_at"] = expires_at
        if locale is not None:
            _body["locale"] = locale
        if merchant_data is not None:
            _body["merchant_data"] = merchant_data
        if merchant_reference1 is not None:
            _body["merchant_reference1"] = merchant_reference1
        if merchant_reference2 is not None:
            _body["merchant_reference2"] = merchant_reference2
        if merchant_urls is not None:
            _body["merchant_urls"] = merchant_urls
        if options is not None:
            _body["options"] = options
        if order_amount is not None:
            _body["order_amount"] = order_amount
        if order_lines is not None:
            _body["order_lines"] = order_lines
        if order_tax_amount is not None:
            _body["order_tax_amount"] = order_tax_amount
        if payment_method_categories is not None:
            _body["payment_method_categories"] = payment_method_categories
        if purchase_country is not None:
            _body["purchase_country"] = purchase_country
        if purchase_currency is not None:
            _body["purchase_currency"] = purchase_currency
        if shipping_address is not None:
            _body["shipping_address"] = shipping_address
        if status is not None:
            _body["status"] = status
        if intent is not None:
            _body["intent"] = intent
        args.body = _body
        return args

    async def _acreate_session_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments/v1/sessions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_session_create.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_session_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payments/v1/sessions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_session_create.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateSessionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_session(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_session_mapped_args(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
        )
        return await self._acreate_session_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_session(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_session_mapped_args(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
        )
        return self._create_session_oapg(
            body=args.body,
        )

class CreateSession(BaseApi):

    async def acreate_session(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MerchantSessionPydantic:
        raw_response = await self.raw.acreate_session(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
            **kwargs,
        )
        if validate:
            return MerchantSessionPydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantSessionPydantic, raw_response.body)
    
    
    def create_session(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MerchantSessionPydantic:
        raw_response = self.raw.create_session(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
        )
        if validate:
            return MerchantSessionPydantic(**raw_response.body)
        return api_client.construct_model_instance(MerchantSessionPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_session_mapped_args(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
        )
        return await self._acreate_session_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        order_amount: int,
        order_lines: typing.List[OrderLine],
        purchase_country: str,
        purchase_currency: str,
        acquiring_channel: typing.Optional[str] = None,
        attachment: typing.Optional[Attachment] = None,
        authorization_token: typing.Optional[str] = None,
        billing_address: typing.Optional[Address] = None,
        client_token: typing.Optional[str] = None,
        custom_payment_method_ids: typing.Optional[SessionCreateCustomPaymentMethodIds] = None,
        customer: typing.Optional[Customer] = None,
        design: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        locale: typing.Optional[str] = None,
        merchant_data: typing.Optional[str] = None,
        merchant_reference1: typing.Optional[str] = None,
        merchant_reference2: typing.Optional[str] = None,
        merchant_urls: typing.Optional[MerchantUrls] = None,
        options: typing.Optional[Options] = None,
        order_tax_amount: typing.Optional[int] = None,
        payment_method_categories: typing.Optional[typing.List[PaymentMethodCategory]] = None,
        shipping_address: typing.Optional[Address] = None,
        status: typing.Optional[str] = None,
        intent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_session_mapped_args(
            order_amount=order_amount,
            order_lines=order_lines,
            purchase_country=purchase_country,
            purchase_currency=purchase_currency,
            acquiring_channel=acquiring_channel,
            attachment=attachment,
            authorization_token=authorization_token,
            billing_address=billing_address,
            client_token=client_token,
            custom_payment_method_ids=custom_payment_method_ids,
            customer=customer,
            design=design,
            expires_at=expires_at,
            locale=locale,
            merchant_data=merchant_data,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            merchant_urls=merchant_urls,
            options=options,
            order_tax_amount=order_tax_amount,
            payment_method_categories=payment_method_categories,
            shipping_address=shipping_address,
            status=status,
            intent=intent,
        )
        return self._create_session_oapg(
            body=args.body,
        )

