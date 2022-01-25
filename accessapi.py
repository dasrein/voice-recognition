#!/usr/bin/env python3

from pprint import pprint
import iot_api_client as iot
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration
import gettoken
import os
from dotenv import load_dotenv

load_dotenv()

# configure and instance the API client
client_config = Configuration(host="https://api2.arduino.cc/iot")
client_config.access_token = gettoken.token.get("access_token")
client = iot.ApiClient(client_config)
properties_api = iot.PropertiesV2Api(client)

deviceid = os.getenv("DEVICE_ID")
thingid = os.getenv("THING_ID")
propertyid = os.getenv("PROPERTY_ID")  # wallLight

deviceid2 = os.getenv("DEVICE_ID2")
thingid2 = os.getenv("THING_ID2")
propertyid2 = os.getenv("PROPERTY_ID")  # ceilingLight

ON = {"value": True}
OFF = {"value": False}

# toggleOn = properties_api.properties_v2_publish(thingid, propertyid, ON, async_req=True)
# toggleOff = properties_api.properties_v2_publish(thingid, propertyid, OFF, async_req=True)


def getValue():
    return properties_api.properties_v2_show(thingid2, propertyid2).last_value


def toggle(value):
    try:
        # properties_api.properties_v2_publish(thingid,propertyid,value)
        properties_api.properties_v2_publish(thingid2, propertyid2, value)

    except ApiException as e:
        print("Got an exception: {}".format(e))
