# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from klarna_payments_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PAYMENTS_V1_SESSIONS = "/payments/v1/sessions"
    PAYMENTS_V1_SESSIONS_SESSION_ID = "/payments/v1/sessions/{session_id}"
    PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN = "/payments/v1/authorizations/{authorizationToken}"
    PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_ORDER = "/payments/v1/authorizations/{authorizationToken}/order"
    PAYMENTS_V1_AUTHORIZATIONS_AUTHORIZATION_TOKEN_CUSTOMERTOKEN = "/payments/v1/authorizations/{authorizationToken}/customer-token"
