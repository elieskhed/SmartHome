from device import Device
import json

class HumiditySensor(Device):
    def __init__(self, house_name, house_token ,device_id, device_name, device_location, humidity_level):
        """
        Initialise un capteur d'humidité.

        :param device_id: ID unique de l'appareil
        :param device_name: Nom de l'appareil
        :param device_location: Emplacement de l'appareil
        :param humidity_level: Niveau d'humidité actuel
        """
        super().__init__(house_name, house_token ,device_id, device_name, device_location, 'houses/'+str(house_name)+'/TYPE_HUMIDITY/'+device_name, 'humidity_sensor')
        self.humidity_level = humidity_level

    def convertDataToJSON(self):
        """
        Retourne les données du capteur d'humidité en format JSON.
        """
        data = {
            "house_name" : self.house_name,
            "house_token": self.house_token,
            "device_name": self.device_name,
            "device_id": self.device_id,
            "device_location": self.device_location,
            "type": self.device_type,
            "values": {
                "humidity_level": self.humidity_level
            }
        }
        return json.dumps(data)  # Conversion en JSON
