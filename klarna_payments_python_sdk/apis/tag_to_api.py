import typing_extensions

from klarna_payments_python_sdk.apis.tags import TagValues
from klarna_payments_python_sdk.apis.tags.payment_api import PaymentApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PAYMENT: PaymentApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PAYMENT: PaymentApi,
    }
)
