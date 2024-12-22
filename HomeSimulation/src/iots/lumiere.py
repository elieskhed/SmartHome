from device import Device
import json

class Light(Device):
    def __init__(self, device_id, device_name, device_location, state):
        super().__init__(device_id, device_name, device_location, 'device/light')
        self.state = state
        

    def convertDataToJSON(self):
        data = {
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "values": {
                "state": self.state
            }
        }
        return json.dumps(data)
