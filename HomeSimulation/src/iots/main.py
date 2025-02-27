from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House
from carbon_sensor import CarbonSensor
from temperature import Temperature

# IP ou nom de domaine du Broker
# PORT port par défaut 1883 (pour le tests (attention pas sécuriséé))
BROKER = '172.20.10.2'
#PORT   = 1883
PORT = 8883

ca_cert     = './certs/CA/ca.crt'
client_cert = './certs/clients/client.crt'
client_key  = './certs/clients/client.key'

#création des différents nombres aléatoires?


#création des différentes devices/capteurs pour l'analyse
devices = [
    Light("eliesHouse", 1, 'lamp_kit', 'kitchen'),
    HumiditySensor("eliesHouse", 2, 'humid_sens', 'kitchen'),
    CarbonSensor("eliesHouse", 3, 'carb_sens', 'garage'),
    Temperature("eliesHouse", 4, 'temp_sens', 'out_entry')
]
# devices = [
#     CarbonSensor(1, 'carb_sens', 'garage')
# ]

#création de la maison et envoie des données des capteurs/de la maison
house = House(devices, BROKER, PORT)

# Tests PORT 1883
# house.sendAllDataPeriodically(5)
#house.printAllDataPeriodically(1)

# Tests PORT 8883
house.sendAllSecurisedDatasPeriodically(5, client_cert, client_key, ca_cert)