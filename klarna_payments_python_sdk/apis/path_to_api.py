import typing_extensions

from klarna_payments_python_sdk.paths import PathValues
from klarna_payments_python_sdk.apis.paths.payments_v1_sessions import PaymentsV1Sessions
from klarna_payments_python_sdk.apis.paths.payments_v1_sessions_session_id import PaymentsV1SessionsSessionId
from klarna_payments_python_sdk.apis.paths.payments_v1_authorizations_authorization_token import PaymentsV1AuthorizationsAuthorizationToken
from klarna_payments_python_sdk.apis.paths.payments_v1_authorizations_authorization_token_order import PaymentsV1AuthorizationsAuthorizationTokenOrder
from klarna_payments_python_sdk.apis.paths.payments_v1_authorizations_authorization_token_customer_token import PaymentsV1AuthorizationsAuthorizationTokenCustomerToken

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PAYMENTS_V1_SESSIONS: PaymentsV1Sessions,
        PathValues.PAYMENTS_V1_SESSIONS_SESSION_ID: PaymentsV1SessionsSessionId,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN: PaymentsV1AuthorizationsAuthorizationToken,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_ORDER: PaymentsV1AuthorizationsAuthorizationTokenOrder,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_CUSTOMERTOKEN: PaymentsV1AuthorizationsAuthorizationTokenCustomerToken,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PAYMENTS_V1_SESSIONS: PaymentsV1Sessions,
        PathValues.PAYMENTS_V1_SESSIONS_SESSION_ID: PaymentsV1SessionsSessionId,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN: PaymentsV1AuthorizationsAuthorizationToken,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_ORDER: PaymentsV1AuthorizationsAuthorizationTokenOrder,
        PathValues.PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_CUSTOMERTOKEN: PaymentsV1AuthorizationsAuthorizationTokenCustomerToken,
    }
)
