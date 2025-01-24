from device import Device
import json
import random

class Temperature(Device):
    def __init__(self, house_name, device_id, device_name, device_location):
        super().__init__(house_name, device_id, device_name, device_location, 'device/temperature')
        self.device_value = 12
        
    def setRandomValue(self):
        self.device_value += (random.randint(-10,10)/10)

    def convertDataToJSON(self):
        data = {
            "house_name": self.house_name,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "type": self.device_type,
            "values": {
                "state": self.device_value
            }
        }
        return json.dumps(data)
