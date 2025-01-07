from device import Device
import json
import random

class AlarmeSystem(Device):
    def __init__(self, device_id, device_name, device_location):
        super().__init__(device_id, device_name, device_location, 'device/alarme/noise')
        self.device_value = 0 # alarme off, non activée, si 1 alors alarme activée par le user
    
    def setRandomValue(self):{}
        

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
