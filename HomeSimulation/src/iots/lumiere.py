from device import Device
import json
import random

# Topic 

class Light(Device):
    def __init__(self, house_name, house_token ,device_id, device_name, device_location, state):
        super().__init__(house_name, house_token ,device_id, device_name, device_location, 'houses/'+str(house_name)+'/TYPE_LIGHT/'+device_name, 'light_sensor')
        self.state = state

    def setRandomValue(self):
        self.state = random.choice([1, 0])
    

    def convertDataToJSON(self):
        data = {
            "house_name": self.house_name,
            "house_token": self.house_token,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "type": self.device_type,
            "values": {
                "state": self.state
            }
        }
        return json.dumps(data)
