from humidity_sensor import HumiditySensor
from lumiere import Light
from house import House

BROKER = '172.20.10.5'
PORT   = 1883

devices = [
    Light(1, 'lamp_kit', 'kitchen', False),
    HumiditySensor(1, 'humid_sens', 'kitchen', 0.12)
]

house = House(devices, BROKER, PORT)
house.sendAllDataPeriodically(5)