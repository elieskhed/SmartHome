from device import Device
import paho.mqtt.client as mqtt
import time


class House:
    def __init__(self, devices, broker, port=1883):
        self.devices = devices
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()

    def add_device(self, device):
        self.devices.append(device)

    def sendAllDatas(self):
        try:
            self.client.connect(self.broker, self.port)
            for device in self.devices:
                self.client.publish(device.device_topic, device.convertDataToJSON())
                print("Message published: " + str(device))
            self.client.disconnect()
        except Exception as e:
            print(f"Error while sending data: {e}")

    def sendAllDataPeriodically(self, period):
        while True:
            try:
                self.sendAllDatas()
                time.sleep(period)
            except Exception as e:
                print(f"Error during periodic data sending: {e}")


    def sendAllSecurisedDatas(self, cert_path, pKey_path, ca_cert_path):
        """
        Sends all device data securely using TLS/SSL for encryption.

        Args:
            cert_path (str): Path to the client certificate file.
            pKey_path (str): Path to the client private key file.
            ca_cert_path (str): Path to the CA certificate file.
        """
        try:
            # Configure the MQTT client to use TLS/SSL if not already configured
            if not hasattr(self.client, '_ssl_context') or not self.client._ssl_context:
                self.client.tls_set(
                    ca_certs=ca_cert_path,    # Path to the CA certificate file
                    certfile=cert_path,       # Client certificate path
                    keyfile=pKey_path         # Client private key path
                )
                self.client.tls_insecure_set(True)  # For testing purposes (not for production)

            # Connect securely to the broker if not already connected
            if not self.client.is_connected():
                self.client.connect(self.broker, self.port)

            # Publish the data securely
            for device in self.devices:
                topic = device.device_topic
                message = device.convertDataToJSON()
                print(f"Publishing to {topic}: {message}")
                self.client.publish(topic, message, qos=1)
        except Exception as e:
            print(f"Error while sending secure data: {e}")

    def sendAllSecurisedDatasPeriodically(self, period, cert_path, pKey_path, ca_cert_path):
        """
        Periodically sends all device data securely using TLS/SSL for encryption.

        Args:
            period (int): Interval between data sending (in seconds).
            cert_path (str): Path to the client certificate file.
            pKey_path (str): Path to the client private key file.
            ca_cert_path (str): Path to the CA certificate file.
        """
        try:
            # Ensure secure connection is configured
            self.sendAllSecurisedDatas(cert_path, pKey_path, ca_cert_path)

            # Periodically publish data
            while True:
                for device in self.devices:
                    topic = device.device_topic
                    message = device.convertDataToJSON()
                    print(f"Publishing to {topic}: {message}")
                    self.client.publish(topic, message, qos=1)
                time.sleep(period)
        except Exception as e:
            print(f"Error during periodic secure data sending: {e}")
        finally:
            # Disconnect from the broker
            if self.client.is_connected():
                self.client.disconnect()
