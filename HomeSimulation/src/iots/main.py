from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House

# IP ou nom de domaine du Broker
# PORT port par défaut 1883 (pour le tests (attention pas sécuriséé))
BROKER = '172.20.10.5'
# PORT   = 1883
PORT = 8883

# Auhentification de la maison, et association de celle-ci avec
# Les informations du Propriétaire récupéré depuis SmartHomeAPI.
ca_cert     = './certs/CA/ca.crt'
client_cert = './certs/clients/client.crt'
client_key  = './certs/clients/client.key'
house_token = "1CMaPGPNA0ZH8wwkWHcHrdQtHpv1fipAnQolMLYL"
house_name = "housename"

devices = [
    Light(house_name, house_token,1, 'lamp_kit', 'kitchen', 0),
    HumiditySensor(house_name, house_token,1, 'humid_sens', 'kitchen', 0.12)
]

house = House(devices, BROKER, PORT)

# Tests PORT 1883
# house.sendAllDataPeriodically(5)

# Tests PORT 8883
house.sendAllSecurisedDatasPeriodically(5, client_cert, client_key, ca_cert)