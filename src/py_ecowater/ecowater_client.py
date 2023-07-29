import datetime
import time
from typing import Optional, List

import requests as r
import logging
from . import constants
from .constants import EcowaterConstants
from .model import UserProfile, Devices, Systems, SystemState


class EcowaterClient(object):
    def __init__(self, username: str, password: str, host: Optional[str] = None):
        self.username: str = username
        self.password: str = password
        self.logger: logging.Logger = logging.getLogger("py_ecowater")
        self.auth_token: str = ""
        self.auth_expiration: Optional[datetime.datetime] = None
        self.devices: Optional[Devices] = None
        self.ecowater_constants: EcowaterConstants = EcowaterConstants(host)

    def __authenticate(self) -> bool:
        if self.auth_token and self.auth_expiration:
            if datetime.datetime.now() + datetime.timedelta(days=10) > self.auth_expiration:
                self.logger.info("The Auth token expires within 10 days, need to refresh")
                self.auth_token = ""
                self.auth_expiration = None
            else:
                return True
        else:
            self.logger.info("Using credentials to fetch auth token")

        body = {
            "username": self.username,
            "password": self.password
        }

        url = ""
        try:
            url = f"{self.ecowater_constants.uri_base}{constants.ECOWATER_PATH_AUTH}"
            headers = self.ecowater_constants.headers_auth
            response = r.post(url, headers=headers, json=body)
        except Exception as e:
            self.logger.error("Unable to authenticate to %s: %s", url, e)
            return False

        if response.status_code != 200:
            self.logger.error("Auth response code was %s: %s", response.status_code, response.reason)
            return False

        try:
            auth_response = response.json()
        except Exception as e:
            self.logger.error("Could not parse json from auth response: %s. %s", response.content, e)
            return False

        if "data" in auth_response:
            data = auth_response["data"]

            if "token" in data:
                self.auth_token = data["token"]
            if "expiresIn" in data:
                self.auth_expiration = datetime.datetime.now() + datetime.timedelta(milliseconds=data["expiresIn"])
            if "deviceMap" in data:
                self.devices: Optional[Devices] = Devices(data["deviceMap"])

        if self.auth_token:
            return True
        else:
            self.logger.error("Could not find auth token in response from auth endpoint")
            return False

    def get_devices(self) -> Devices:
        self.__authenticate()
        return self.devices

    def get_user_profile(self) -> UserProfile:
        return self.__get_api(UserProfile)

    def get_systems(self) -> Systems:
        return self.__get_api(Systems)

    def get_system_state(self, serial_number: str):
        return self.__get_api(SystemState, serial_number=serial_number)

    def __get_api(self, klass, **kwargs):
        self.__authenticate()

        path = klass.get_path(**kwargs)

        url = ""
        try:
            url = f"{self.ecowater_constants.uri_base}{path}"
            headers = self.ecowater_constants.headers_api.copy()
            headers["authorization"] = f"Bearer {self.auth_token}"

            response = r.get(url, headers=headers)
        except Exception as e:
            self.logger.error("Unable to authenticate to %s: %s", url, e)
            return False

        if response.status_code != 200:
            self.logger.error("Response code was %s: %s", response.status_code, response.reason)
            return False

        try:
            response_json = response.json()
        except Exception as e:
            self.logger.error("Could not parse json from response: %s. %s", response.content, e)
            return False

        if "data" in response_json:
            return klass(api=response_json["data"])
        else:
            return None


if __name__ == "__main__":
    import sys, os

    date_strftime_format = "%y-%b-%d %H:%M:%S"
    message_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=message_format, datefmt=date_strftime_format, stream=sys.stdout)

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    client = EcowaterClient(username, password)
    devices = client.get_devices()
    profile = client.get_user_profile()
    systems = client.get_systems()
    system_state = client.get_system_state(systems.systems[0].serial_number)
