from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House

# IP ou nom de domaine du Broker
# PORT port par défaut 1883 (pour le tests (attention pas sécuriséé))
BROKER = '172.20.10.3'
PORT   = 1883

devices = [
    Light(1, 'lamp_kit', 'kitchen', False),
    HumiditySensor(1, 'humid_sens', 'kitchen', 0.12)
]

house = House(devices, BROKER, PORT)
house.sendAllDataPeriodically(5)
