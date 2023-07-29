# py_ecowater
![Current Version](https://img.shields.io/badge/Version-0.1.1-brightgreen)

A python library for getting device data from Ecowater API for devices such as the Rheem RHW42 water softener, which 
provides WI-FI connectivity via the iQua app.

## Installation

```bash
pip install py_ecowater
```

## Usage
The primary class is `EcowaterClient`.  It takes two parameters, `username` and `password`.  
These are the same credentials you use to log in to the app. The primary methods are `get_devices`, `get_user_profile`, 
`get_systems`, and `get_system_state`.  

The `get_system_state` method takes a single parameter, `serial_number`, which is the serial number of the system you 
want to get the state of and can be found from the system information returned by `get_systems`.  

The methods return python objects that can be accessed as attributes. 

```python
import os
from py_ecowater import EcowaterClient

username = os.environ.get('ECOWATER_USERNAME')
password = os.environ.get('ECOWATER_PASSWORD')

client = EcowaterClient(username, password)

devices = client.get_devices()
'''
{
  "devices": [
    {
      "id": 12345,
      "email": "myemail@test.com",
      "type": "AC",
      "status": "READY",
      "role": "user",
      "user_uuid": null,
      "dealer_id": null,
      "members": null,
      "alerts_ack": null,
      "mydata": null,
      "date": 1650692107704,
      "created_by": "user"
    }
  ]
}
'''

profile = client.get_user_profile()
'''
{
  "id": "<unique id>",
  "name": "Bob,Ross",
  "email": "myemail@test.com",
  "company": {
    "phone_country_code": "",
    "phone": "1234567890",
    "primary_phone_code": "",
    "primary_phone": "1234567890",
    "members_count": 2,
    "support_phone": "",
    "support_phone_code": ""
  },
  "phone": "1234567890",
  "time_zone": null,
  "address_line_1": "123 My Addr Rd",
  "address_line_2": "",
  "city": "My City",
  "state": null,
  "zip_code": "98765",
  "country": "US",
  "contact_language": "en",
  "roles": [
    "user"
  ],
  "change_password": false,
  "manufacturer_id": "",
  "first_name": "Bob",
  "last_name": "Ross",
  "meta": {
    "phone_country_code": "",
    "phone": "1234567890",
    "primary_phone_code": "+1",
    "primary_phone": "1234567890",
    "members_count": 2,
    "support_phone": "",
    "support_phone_code": ""
  }
}
'''

systems = client.get_systems()
'''
{
  "systems": [
    {
      "id": "<system id>",
      "serial_number": "SL0<serial number>",
      "nickname": "Water Softener",
      "description": {
        "unit_owner": "customer",
        "rental_access": 1
      },
      "ac_role_name": "User",
      "role": "user",
      "model_id": "<model id>",
      "model_name": "108201",
      "model_description": "Rheem RHW42",
      "system_type": "demand softener",
      "dealer_access": false,
      "alarms_alerts": false,
      "is_rental": false,
      "is_restricted": false,
      "alerts_active": null,
      "is_super_hero": false,
      "is_filter_system": false,
      "product_image": "Rheem",
      "water_shut_off_valve_control": true
    }
  ]
}

'''

system_state = client.get_system_state(systems.systems[0].serial_number)
'''
{
  "iron_level_tenths_ppm": {
    "value": 0
  },
  "hardness_unit_enum": {
    "value": 0
  },
  "hardness_grains": {
    "value": 11
  },
  "salt_level_tenths": {
    "value": 20,
    "percent": 25
  },
  "salt_monitor_enum": {
    "value": 1
  },
  "volume_unit_enum": {
    "value": 0
  },
  "regen_enable_enum": {
    "value": 1
  },
  "regen_time_secs": {
    "value": 7200
  },
  "time_format_enum": {
    "value": 0
  },
  "time_zone_enum": {
    "value": "America/Denver"
  },
  "date_format_enum": {
    "value": 0
  },
  "water_shutoff_valve_req": {
    "value": 0
  },
  "total_water_available_gallons": {
    "value": 2224
  },
  "current_water_flow": {
    "value": 0.0
  },
  "gallons_used_today": {
    "value": 38
  },
  "average_daily_use_gallons": {
    "value": 90
  },
  "regen_status_enum": {
    "value": 0
  },
  "out_of_salt_estimated_days": {
    "value": 130
  },
  "days_since_last_regen": {
    "value": 14
  },
  "model_id": {
    "value": <model id>
  },
  "model_description": {
    "value": "Rheem RHW42"
  },
  "system_type": {
    "value": "demand softener",
    "type": "softener"
  },
  "water_shutoff_valve": {
    "value": 0
  },
  "water_shutoff_valve_installed": {
    "value": 1
  },
  "water_shutoff_valve_override": {
    "value": 0
  },
  "water_shutoff_valve_device_action": {
    "value": 0
  },
  "water_shutoff_valve_error_code": {
    "value": 0
  },
  "base_software_version": {
    "value": "r4.4 MPC01082"
  },
  "power": "Online",
  "device_date": "2023-07-29T09:44:38.149000",
  "refresh_policy": {
    "delay": "low",
    "time": 300000
  }
}
'''
```

## Contributing and Development

### Update git-submod-lib submodule for current Makefile Targets
```shell
git submodule update --init --remote
```

### Make Python venv and install requirements
```shell
make -f git-submod-lib/makefile/Makefile venv
```

Make and commit changes, and then build locally as follows.

### Build Locally
```shell
make -f git-submod-lib/makefile/Makefile build-python
```

### Make a pull request to `main` with your changes
```shell
make -f git-submod-lib/makefile/Makefile pull-request-main
```

## Releasing

### Minor releases
```shell
make -f git-submod-lib/makefile/Makefile promotion-alpha
```

Once the PR is approved and merged:
```shell
make -f git-submod-lib/makefile/Makefile github-release
```

Once the Release is published:
```shell
make -f git-submod-lib/makefile/Makefile twine-upload
```

Now cut a version release branch:
```shell
make -f git-submod-lib/makefile/Makefile github-branch
```

Now move `main` to the next `alpha` version to capture future development
```shell
make -f git-submod-lib/makefile/Makefile version-alpha
```

### Patch releases
Start with the version branch to be patched (ie `0.0.x`)
```shell
make -f git-submod-lib/makefile/Makefile promotion-patch
```

Once the PR is approved and merged:
```shell
make -f git-submod-lib/makefile/Makefile github-release-patch
```

Once the Patch Release is published:
```shell
make -f git-submod-lib/makefile/Makefile twine-upload
```
