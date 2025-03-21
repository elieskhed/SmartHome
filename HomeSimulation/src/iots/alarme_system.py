from device import Device
import json
import random

class AlarmeSystem(Device):
    def __init__(self, device_id, device_name, device_location):
        super().__init__(device_id, device_name, device_location, 'device/alarme/noise')
        self.device_value = 0 # alarme off, non activée, si 1 alors alarme activée par le user
    
    def setRandomValue(self):
        r = random.randint(0, 100)
        if(self.device_value == 1):
            if(r<=70):
                self.device_value = 1
            else:
                self.device_value = 0
        else:
            if(r<=40):
                self.device_value = 1
            else:
                self.device_value = 0
        

    def convertDataToJSON(self):
        data = {
            "house_name": self.house_name,
            "house_token": self.house_token,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "type": self.device_type,
            "values": {
                "alarm_system_value": self.device_value
            }
        }
        return json.dumps(data)