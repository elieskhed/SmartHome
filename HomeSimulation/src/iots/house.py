from device import Device
import paho.mqtt.client as mqtt
import time


class House:
    def __init__(self, devices, broker, port=1883):
        self.devices = devices
        self.broker  = broker
        self.port    = port
        self.client = mqtt.Client()
        self.client.connect(broker, port)

    def add_device(self, device):
        self.devices.append(device)
    
    def sendAllDatas(self):
        for device in self.devices:
            self.client.publish(device.device_topic, device.convertDataToJSON())
            print("Message publiée: " + str(device))

    def sendAllDataPeriodically(self, period):
        while 1:
            self.sendAllDatas()
            time.sleep(period)
