ECOWATER_HOST = "apioem.ecowater.com"
ECOWATER_PATH_AUTH = "v1/auth/signin"
ECOWATER_PATH_USER_PROFILE = "v1/user/profile"
ECOWATER_PATH_SYSTEMS = "v1/system"
ECOWATER_PATH_SYSTEM_STATE = f"{ECOWATER_PATH_SYSTEMS}/%s/dashboard"

ECOWATER_HEADERS = {
    "connection": "keep-alive",
    "accept": "application/json, text/plain, */*",
    "user-agent": "iQua/3 CFNetwork/1333.0.4 Darwin/21.5.0",
    "accept-language": "en-us",
    "accept-encoding": "gzip, deflate, br"
}


class EcowaterConstants(object):
    def __init__(self, host=ECOWATER_HOST):
        self.host = host if host else ECOWATER_HOST
        self.uri_base = f"https://{self.host}/"
        self.headers_api = ECOWATER_HEADERS.copy()
        self.headers_api["host"] = self.host
        self.headers_auth = ECOWATER_HEADERS.copy()
        self.headers_auth["content-type"] = "application/json;charset=utf-8"
