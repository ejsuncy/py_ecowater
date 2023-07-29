import logging
import json
from datetime import datetime

from typing import List, Optional

from . import constants

logger = logging.getLogger("py_ecowater")


class ApiResponse(object):
    """A base class object representing an API response."""

    def __init__(self):
        pass

    @staticmethod
    def get_path(**kwargs) -> Optional[str]:
        return None


class ApiResponseObject(ApiResponse):
    """An object representing an API response.
    Parameters
    ----------
    api : `dict`
        A python dict generated from `response.json()`
    """

    def __init__(self, api: dict = None):
        super().__init__()


class ApiResponseObjectList(ApiResponse):
    """An object representing an API response that is a list of objects.
    Parameters
    ----------
    api : `list`
        A python list generated from `response.json()`
    """

    def __init__(self, api: list = None):
        super().__init__()


class UserProfile(ApiResponseObject):
    """An object representing an Ecowater User Profile.
    Parameters
    ----------
    api : `dict`
        A python dict generated from `response.json()`
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.id: str = api["id"] if "id" in api else None
            self.name: str = api["name"] if "name" in api else None
            self.email: str = api["email"] if "email" in api else None
            self.company: Company = Company(api=api["companyName"]) if "companyName" in api else None
            self.phone: str = api["phone"] if "phone" in api else None
            self.time_zone: str = api["timeZone"] if "timeZone" in api else None
            self.time_zone = None if self.time_zone == "-" else self.time_zone
            self.address_line_1: str = api["addressLine1"] if "addressLine1" in api else None
            self.address_line_2: str = api["addressLine2"] if "addressLine2" in api else None
            self.city: str = api["city"] if "city" in api else None
            self.state: str = api["state"] if "state" in api else None
            self.state = None if self.state == "-" else self.state
            self.zip_code: str = api["zipCode"] if "zipCode" in api else None
            self.country: str = api["country"] if "country" in api else None
            self.contact_language: str = api["contactLanguage"] if "contactLanguage" in api else None
            self.roles: List[str] = api["roles"] if "roles" in api else []
            self.change_password: bool = bool(api["change_password"]) if "change_password" in api else False
            self.manufacturer_id: str = api["manufacturer_id"] if "manufacturer_id" in api else None
            self.first_name: str = api["firstName"] if "firstName" in api else None
            self.last_name: str = api["lastName"] if "lastName" in api else None
            self.meta: Meta = Meta(api["meta"]) if "meta" in api else None

    @staticmethod
    def get_path(**kwargs) -> Optional[str]:
        return constants.ECOWATER_PATH_USER_PROFILE


class Company(object):
    """An object representing an Ecowater Company.
    Parameters
    ----------
    api : `str`
        A JSON string
    """
    def __init__(self, api: str = None):
        if api:
            try:
                company_dict = json.loads(api)
            except Exception as e:
                logger.error("Unable to parse companyName string ('%s') as json: %s", api, e)
                return

            self.phone_country_code: str = company_dict["phoneCountryCode"] if "phoneCountryCode" in company_dict else None
            self.phone: str = company_dict["phone"] if "phone" in company_dict else None
            self.primary_phone_code: str = company_dict["primaryPhoneCode"] if "phone" in company_dict else None
            self.primary_phone: str = company_dict["primaryPhone"] if "primaryPhone" in company_dict else None
            self.members_count: int = int(company_dict["membersCount"]) if "membersCount" in company_dict else None
            self.support_phone: str = company_dict["supportPhone"] if "supportPhone" in company_dict else None
            self.support_phone_code: str = company_dict["supportPhoneCode"] if "supportPhoneCode" in company_dict else None


class Meta(ApiResponseObject):
    """An object representing Ecowater User Profile Metadata.
    Parameters
    ----------
    api : `dict`
        A python dict generated from `response.json()`
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.phone_country_code: str = api["phoneCountryCode"] if "phoneCountryCode" in api else None
            self.phone: str = api["phone"] if "phone" in api else None
            self.primary_phone_code: str = api["primaryPhoneCode"] if "primaryPhoneCode" in api else None
            self.primary_phone: str = api["primaryPhone"] if "primaryPhone" in api else None
            self.members_count: int = int(api["membersCount"]) if "membersCount" in api else None
            self.support_phone: str = api["supportPhone"] if "supportPhone" in api else None
            self.support_phone_code: str = api["supportPhoneCode"] if "supportPhoneCode" in api else None

class Devices(ApiResponseObjectList):
    """An object representing a list of Ecowater Devices
    Parameters
    ----------
    api : `list`
        A python list generated from `response.json()`
    """
    def __init__(self, api: list = None):
        super().__init__(api)

        self.devices: List[Device] = []

        if api:
            for dev in api:
                if dev:
                    self.devices.append(Device(dev))

class Device(ApiResponseObject):
    """An object representing an Ecowater Device.
    Parameters
    ----------
    api : `dict`
        A python dict generated from `response.json()`
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.id: int = api["id"] if "id" in api else None
            self.email: str = api["email"] if "email" in api else None
            self.type: str = api["type"] if "type" in api else None
            self.status: str = api["status"] if "status" in api else None
            self.role: str = api["role"] if "role" in api else None
            self.user_uuid: any = api["user_uuid"] if "user_uuid" in api else None
            self.dealer_id: any = api["dealer_id"] if "dealer_id" in api else None
            self.members: any = api["members"] if "members" in api else None
            self.alerts_ack: any = api["alerts_ack"] if "alerts_ack" in api else None
            self.mydata: any = api["mydata"] if "mydata" in api else None
            self.date: int = api["date"] if "date" in api else None
            self.created_by: str = api["createdBy"] if "createdBy" in api else None


class Systems(ApiResponseObjectList):
    """An object representing a list of Ecowater Systems
    Parameters
    ----------
    api : `list`
        A python list generated from `response.json()`
    """
    def __init__(self, api: list = None):
        super().__init__(api)

        self.systems: List[System] = []

        if api:
            for sys in api:
                if sys:
                    self.systems.append(System(sys))

    @staticmethod
    def get_path(**kwargs) -> Optional[str]:
        return constants.ECOWATER_PATH_SYSTEMS


class System(ApiResponseObject):
    """Ecowater System Device, such as a Rheem Water Softener.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.id: str = api["id"] if "id" in api else None
            self.serial_number: str = api["serialNumber"] if "serialNumber" in api else None
            self.nickname: str = api["nickname"] if "nickname" in api else None
            self.description: SystemDescription = SystemDescription(api["description"]) if "description" in api else None
            self.ac_role_name: str = api["acRoleName"] if "acRoleName" in api else None
            self.role: str = api["role"] if "role" in api else None
            self.model_id: str = api["modelId"] if "modelId" in api else None
            self.model_name: str = api["modelName"] if "modelName" in api else None
            self.model_description: str = api["modelDescription"] if "modelDescription" in api else None
            self.system_type: str = api["systemType"] if "systemType" in api else None
            self.dealer_access: bool = api["dealerAccess"] if "dealerAccess" in api else None
            self.alarms_alerts: bool = api["alarmsAlerts"] if "alarmsAlerts" in api else None
            self.is_rental: bool = api["isRental"] if "isRental" in api else None
            self.is_restricted: bool = api["isRestricted"] if "isRestricted" in api else None
            self.alerts_active: bool = api["alertsActive"] if "alertsActive" in api else None
            self.is_super_hero: bool = api["isSuperHero"] if "isSuperHero" in api else None
            self.is_filter_system: bool = api["isFilterSystem"] if "isFilterSystem" in api else None
            self.product_image: str = api["productImage"] if "productImage" in api else None
            self.water_shut_off_valve_control: bool = api["wsovControl"] if "wsovControl" in api else None


class SystemDescription(object):
    """Ecowater System Description.
    Parameters
    ----------
    api : `str`
        A JSON string.
    """

    def __init__(self, api: str = None):
        if api:
            try:
                description_dict = json.loads(api)
            except Exception as e:
                logger.error("Unable to parse description string ('%s') as json: %s", api, e)
                return

            self.unit_owner = description_dict["unitOwner"] if "unitOwner" in description_dict else None
            self.rental_access = description_dict["rentalAccess"] if "rentalAccess" in description_dict else None


class SystemState(ApiResponseObject):
    """An object representing an Ecowater System State. This data is mostly used for the app dashboard and is called
    frequently in the app (every 2 seconds by default).
    Parameters
    ----------
    api : `dict`
        A python dict generated from `response.json()`
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.iron_level_tenths_ppm: IronLevelTenthsPpm = IronLevelTenthsPpm(api["ironLevelTenthsPpm"]) \
                if "ironLevelTenthsPpm" in api else None
            self.hardness_unit_enum: HardnessUnitEnum = HardnessUnitEnum(api["hardnessUnitEnum"]) \
                if "hardnessUnitEnum" in api else None
            self.hardness_grains: HardnessGrains = HardnessGrains(api["hardnessGrains"]) \
                if "hardnessGrains" in api else None
            self.salt_level_tenths: SaltLevelTenths = SaltLevelTenths(api["saltLevelTenths"]) \
                if "saltLevelTenths" in api else None
            self.salt_monitor_enum: SaltMonitorEnum = SaltMonitorEnum(api["saltMonitorEnum"]) \
                if "saltMonitorEnum" in api else None
            self.volume_unit_enum: VolumeUnitEnum = VolumeUnitEnum(api["volumeUnitEnum"]) \
                if "volumeUnitEnum" in api else None
            self.regen_enable_enum: RegenEnableEnum = RegenEnableEnum(api["regenEnableEnum"]) \
                if "regenEnableEnum" in api else None
            self.regen_time_secs: RegenTimeSecs = RegenTimeSecs(api["regenTimeSecs"]) \
                if "regenTimeSecs" in api else None
            self.time_format_enum: TimeFormatEnum = TimeFormatEnum(api["timeFormatEnum"]) \
                if "timeFormatEnum" in api else None
            self.time_zone_enum: TimeZoneEnum = TimeZoneEnum(api["timeZoneEnum"]) \
                if "timeZoneEnum" in api else None
            self.date_format_enum: DateFormatEnum = DateFormatEnum(api["dateFormatEnum"]) \
                if "dateFormatEnum" in api else None
            self.water_shutoff_valve_req: WaterShutoffValveReq = WaterShutoffValveReq(api["waterShutoffValveReq"]) \
                if "waterShutoffValveReq" in api else None
            self.total_water_available_gallons: TotalWaterAvailableGallons = TotalWaterAvailableGallons(api["totalWaterAvailGals"]) \
                if "totalWaterAvailGals" in api else None
            self.current_water_flow: CurrentWaterFlow = CurrentWaterFlow(api["currentWaterFlow"]) \
                if "currentWaterFlow" in api else None
            self.gallons_used_today: GallonsUsedToday = GallonsUsedToday(api["gallonsUsedToday"]) \
                if "gallonsUsedToday" in api else None
            self.average_daily_use_gallons: AverageDailyUseGallons = AverageDailyUseGallons(api["avgDailyUseGallons"]) \
                if "avgDailyUseGallons" in api else None
            self.regen_status_enum: RegenStatusEnum = RegenStatusEnum(api["regenStatusEnum"]) \
                if "regenStatusEnum" in api else None
            self.out_of_salt_estimated_days: OutOfSaltEstimatedDays = OutOfSaltEstimatedDays(api["outOfSaltEstDays"]) \
                if "outOfSaltEstDays" in api else None
            self.days_since_last_regen: DaysSinceLastRegen = DaysSinceLastRegen(api["daysSinceLastRegen"]) \
                if "daysSinceLastRegen" in api else None
            self.model_id: ModelId = ModelId(api["modelId"]) \
                if "modelId" in api else None
            self.model_description: ModelDescription = ModelDescription(api["modelDescription"]) \
                if "modelDescription" in api else None
            self.system_type: SystemType = SystemType(api["systemType"]) \
                if "systemType" in api else None
            self.water_shutoff_valve: WaterShutoffValve = WaterShutoffValve(api["waterShutoffValve"]) \
                if "waterShutoffValve" in api else None
            self.water_shutoff_valve_installed: WaterShutoffValveInstalled = WaterShutoffValveInstalled(api["waterShutoffValveInstalled"]) \
                if "waterShutoffValveInstalled" in api else None
            self.water_shutoff_valve_override: WaterShutoffValveOverride = WaterShutoffValveOverride(api["waterShutoffValveOverride"]) \
                if "waterShutoffValveOverride" in api else None
            self.water_shutoff_valve_device_action: WaterShutoffValveDeviceAction = WaterShutoffValveDeviceAction(api["waterShutoffValveDeviceAction"]) \
                if "waterShutoffValveDeviceAction" in api else None
            self.water_shutoff_valve_error_code: WaterShutoffValveErrorCode = WaterShutoffValveErrorCode(api["wsovErrorCode"]) \
                if "wsovErrorCode" in api else None
            self.base_software_version: BaseSoftwareVersion = BaseSoftwareVersion(api["baseSoftwareVersion"]) \
                if "baseSoftwareVersion" in api else None
            self.power: str = api["power"] if "power" in api else None
            try:
                self.device_date: datetime = datetime.strptime(api["deviceDate"], "%Y-%m-%dT%H:%M:%S.%fZ") \
                    if "deviceDate" in api else None
            except ValueError:
                logger.error("Unable to parse deviceDate string ('%s') as datetime", api["deviceDate"])
                self.device_date = None
            self.refresh_policy: RefreshPolicy = RefreshPolicy(api["refreshPolicy"]) \
                if "refreshPolicy" in api else None










    @staticmethod
    def get_path(**kwargs) -> Optional[str]:
        serial_number = kwargs["serial_number"] if "serial_number" in kwargs else None

        if not serial_number:
            logger.error("System serial_number parameter is not specified")
            return None

        # noinspection PyStringFormat
        return f"{constants.ECOWATER_PATH_SYSTEM_STATE}" % serial_number


class IronLevelTenthsPpm(ApiResponseObject):
    """Ecowater System State Iron Level measured in tenths of parts per million.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class HardnessUnitEnum(ApiResponseObject):
    """Ecowater System State Hardness Unit Enum. Current meaning unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class HardnessGrains(ApiResponseObject):
    """Ecowater System State Hardness Grain Count
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class SaltLevelTenths(ApiResponseObject):
    """Ecowater System State Salt Level measured in tenths of salt marker notches.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None
            self.percent: int = int(api["percent"]) if "percent" in api else None


class SaltMonitorEnum(ApiResponseObject):
    """Ecowater System State Salt Monitor Enum. Current meaning unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class VolumeUnitEnum(ApiResponseObject):
    """Ecowater System State Volume Unit Enum. Current meaning unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class RegenEnableEnum(ApiResponseObject):
    """Ecowater System State Regen Enable Enum. Current meaning unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class RegenTimeSecs(ApiResponseObject):
    """Ecowater System State Regen Time measured in seconds after midnight. For example, 2am = 7200
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class TimeFormatEnum(ApiResponseObject):
    """Ecowater System State Time Format Enum. Current meaning unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class TimeZoneEnum(ApiResponseObject):
    """Ecowater System State Time Zone Enum. Current valid value set unknown, but an example is "America/Denver"
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: str = api["value"] if "value" in api else None


class DateFormatEnum(ApiResponseObject):
    """Ecowater System State Date Format Enum. Current valid value set unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class WaterShutoffValveReq(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Req. Current valid value set unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class TotalWaterAvailableGallons(ApiResponseObject):
    """Ecowater System State Total Soft Water Available in gallons.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class CurrentWaterFlow(ApiResponseObject):
    """Ecowater System State Current Water Flow in gallons per minute.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: float = float(api["value"]) if "value" in api else None


class GallonsUsedToday(ApiResponseObject):
    """Ecowater System State Gallons Used Today in gallons.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class AverageDailyUseGallons(ApiResponseObject):
    """Ecowater System State Average Daily Use in gallons.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class RegenStatusEnum(ApiResponseObject):
    """Ecowater System State Regen Status Enum. Current valid value set unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class OutOfSaltEstimatedDays(ApiResponseObject):
    """Ecowater System State Estimated Days until out of salt.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class DaysSinceLastRegen(ApiResponseObject):
    """Ecowater System State Days since last regen
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class ModelId(ApiResponseObject):
    """Ecowater System State Model ID
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class ModelDescription(ApiResponseObject):
    """Ecowater System State Model Description
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: str = api["value"] if "value" in api else None


class SystemType(ApiResponseObject):
    """Ecowater System State System Type
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: str = api["value"] if "value" in api else None
            self.type: str = api["type"] if "type" in api else None


class WaterShutoffValve(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Status. 0 is not activated, 1 is activated (water is shut off)
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None


class WaterShutoffValveInstalled(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Installed Status. 0 is not installed, 1 is installed
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """

    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None

class WaterShutoffValveOverride(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Override Status. 0 is not overridden, 1 is overridden. This indicates
    whether the water shutoff valve is overridden by the app or not.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None

class WaterShutoffValveDeviceAction(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Device Action. 0 is not activated, 1 is activated (water is shut off).
    This indicates whether the water shutoff valve is overridden by the device or not. See WaterShutoffValveOverride for
    whether the app has activated the water shutoff valve, and compare that to this value to determine if the device has
    actually activated the water shutoff valve. If they are different, the valve could be in the process of opening or
    closing.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None

class WaterShutoffValveErrorCode(ApiResponseObject):
    """Ecowater System State Water Shutoff Valve Error Code. Current valid value set unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: int = int(api["value"]) if "value" in api else None

class BaseSoftwareVersion(ApiResponseObject):
    """Ecowater System State Base Software Version. Current valid value set unknown.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.value: str = api["value"] if "value" in api else None

class RefreshPolicy(ApiResponseObject):
    """Ecowater System State Refresh Policy. Specified by the server to instruct the client how often to poll for
    updates.
    Parameters
    ----------
    api : `dict`
        API Response object as a python dict.
    """
    def __init__(self, api: dict = None):
        super().__init__(api)

        if api:
            self.delay: str = api["delay"] if "delay" in api else None
            self.time: int = int(api["time"]) if "time" in api else None
