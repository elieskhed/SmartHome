from device import Device
import json
import random

class Light(Device):
    def __init__(self, device_id, device_name, device_location):
        super().__init__(device_id, device_name, device_location, 'device/light')
        #self.device_value = "Off"
        self.device_value = 0
        
    def setRandomValue(self):
        #self.device_value = random.choice(["On", "Off"])
        self.device_value = random.choice([1, 0])

    def convertDataToJSON(self):
        data = {
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "values": {
                "state": self.device_value
            }
        }
        return json.dumps(data)
