from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House
from carbon_sensor import CarbonSensor

# IP ou nom de domaine du Broker
# PORT port par défaut 1883 (pour le tests (attention pas sécuriséé))
# BROKER = '172.20.10.3'
BROKER = '127.0.0.1'
PORT   = 1883

#création des différents nombres aléatoires?


#création des différentes devices/capteurs pour l'analyse
devices = [
    Light(1, 'lamp_kit', 'kitchen'),
    HumiditySensor(2, 'humid_sens', 'kitchen'),
    CarbonSensor(3, 'carb_sens', 'garage')
]
# devices = [
#     CarbonSensor(1, 'carb_sens', 'garage')
# ]

#création de la maison et envoie des données des capteurs/de la maison
house = House(devices, BROKER, PORT)
# house.sendAllDataPeriodically(5)
house.printAllDataPeriodically(1)
