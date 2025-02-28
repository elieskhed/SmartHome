from device import Device
import json
import random

class Temperature(Device):
    def __init__(self, device_id, device_name, device_location):
        super().__init__(device_id, device_name, device_location, 'device/temperature')
        self.temperature_value = 12
        
    def setRandomValue(self):
        self.temperature_value+= (random.randint(-10,10)/10)

    def convertDataToJSON(self):
        data = {
            "house_name": self.house_name,
            "house_token": self.house_token,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "type": self.device_type,
            "values": {
                "temperature_value": self.temperature_value
            }
        }
        return json.dumps(data)