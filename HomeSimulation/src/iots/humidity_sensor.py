from device import Device
import json
import random

class HumiditySensor(Device):
    def __init__(self, device_id, device_name, device_location):
        """
        Initialise un capteur d'humidité.

        :param device_id: ID unique de l'appareil
        :param device_name: Nom de l'appareil
        :param device_location: Emplacement de l'appareil
        :param humidity_level: Niveau d'humidité actuel
        """
        super().__init__(device_id, device_name, device_location, 'device/sensor/humidity')
        self.device_value = 45

    def setRandomValue(self):
            self.device_value += (random.randint(-10,10)/100)

    def convertDataToJSON(self):
        """
        Retourne les données du capteur d'humidité en format JSON.
        """
        data = {
            # "house_name" : self.house_name,
            # "house_token": self.house_token,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            # "type": self.device_type,
            "values": {
                "state": self.device_value
            }
        }
        return json.dumps(data)  # Conversion en JSON
