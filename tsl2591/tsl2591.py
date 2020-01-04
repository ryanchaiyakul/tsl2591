import time
import json

import board
import busio

import adafruit_tsl2591

import stickytoe_device

class TSL2591(stickytoe_device.DEVICE.I2C):

    def execute(self, payload: str):
        cmd_dict = json.loads(payload)  # ValueError handled by caller

        # Initialize the I2C bus.
        i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize the sensor.
        sensor = adafruit_tsl2591.TSL2591(i2c)

        ret = {}

        # Parse cmd_dict
        if cmd_dict.get("lux", False):
            ret["lux"] = sensor.lux
        if cmd_dict.get("infared", False):
            ret["infrared"] = sensor.infrared
        if cmd_dict.get("visible", False):
            ret["visible"] = sensor.visible
        if cmd_dict.get("full_spectrum", False):
            ret["full_spectrum"] = sensor.full_spectrum
        
        return json.dumps(ret)

