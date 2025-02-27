from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House
from carbon_sensor import CarbonSensor
from temperature import Temperature

from alarme_system import AlarmeSystem
from alarme import Alarme
from detector import Detector

# IP ou nom de domaine du Broker
# PORT port par défaut 1883 (pour le tests (attention pas sécuriséé))
BROKER = '172.20.10.3'
# BROKER = '172.20.10.2'
PORT   = 1883

#création des différents nombres aléatoires?


#création des différentes devices/capteurs pour l'analyse
devices = [
    Light(1, 'lamp_kit', 'kitchen'),
    HumiditySensor(2, 'humid_sens', 'kitchen'),
    CarbonSensor(3, 'carb_sens', 'garage'),
    Temperature(4, 'temp_sens', 'out_entry'),
    AlarmeSystem(100, 'alarme_system', 'house'),
    Alarme(101, 'alarme', 'in_entry'),
    Detector(102, 'detector_2', 'entry'),
    Detector(103, 'detector_3', 'entry')
]

house = House(devices, BROKER, PORT)
# 
# Tests PORT 1883

# house.sendAllDataPeriodically(5)
house.printAllDataPeriodically(1)

# Tests PORT 8883
# house.sendAllSecurisedDatasPeriodically(5, client_cert, client_key, ca_cert)

