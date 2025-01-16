from device import Device
import json
import random

class CarbonSensor(Device):
    def __init__(self, device_id, device_name, device_location):
        """
        Initialise un capteur d'humidité.

        :param device_id: ID unique de l'appareil
        :param device_name: Nom de l'appareil
        :param device_location: Emplacement de l'appareil
        :param device_value: Taux de carbon dans l'air
        """
        super().__init__(device_id, device_name, device_location, 'device/sensor/carbon')
        self.device_value = 2
    
    def setRandomValue(self):
        self.device_value += (random.randint(-10,10)/100)

    def convertDataToJSON(self):
        """
        Retourne les données du capteur d'humidité en format JSON.
        """
        data = {
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "values": {
                "carbon_level": self.device_value
            }
        }
        return json.dumps(data)  # Conversion en JSON
