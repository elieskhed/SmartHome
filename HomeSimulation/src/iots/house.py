from device import Device
import paho.mqtt.client as mqtt
import time

class House:
    def __init__(self, devices, broker, port=1883):
        self.devices = devices
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        # self.client.connect(broker, port)

    def add_device(self, device):
        self.devices.append(device)

    def sendAllDatas(self):
        try:
            self.client.connect(self.broker, self.port)
            for device in self.devices:
                device.setRandomValue()
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
    
    def print_tab(self, tab):
        """
        Prints a list of device strings formatted as:
        "device_name - device_id - location - value"
        in a nicely aligned table.
        """
        # Parse each item into columns
        rows = [ [part.strip() for part in item.split(" - ")] for item in tab ]
        
        # Determine the maximum width for each column
        if not rows:
            print("No data to display.")
            return

        num_cols = len(rows[0])
        col_widths = [0] * num_cols
        for row in rows:
            for i, col in enumerate(row):
                col_widths[i] = max(col_widths[i], len(col))
        
        # Create a separator line for better readability
        separator = " | ".join('-' * w for w in col_widths)
        
        # Print the table rows
        for row in rows:
            formatted_row = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(row))
            print(formatted_row)
            print(separator)

    def printAllDataPeriodically(self, period):
        i = 20
        while i > 0:
            tab = []
            for device in self.devices:
                device.setRandomValue()
                tab.append(str(device))
                # print("Message publiée: " + str(device))
            i -= 1
            # self.print_tab(tab)
            # print("\n ---------------------------------------------------- \n")
            # print("\n")
            tab = self.detect(tab)
            self.print_tab(tab) # à remplacer pour l'envoir de données sur api

            print("\n ---------------------------------------------------- \n")
            time.sleep(period)
    
    def detect(self, tab):
        detector_triggered = False
        alarm_system_on = False
        triggered_sensors = []
        for item in tab:
            parts = [p.strip() for p in item.split(" - ")]
            if len(parts) != 4:
                continue  # Skip malformed entries
            device_name, device_id, location, value = parts
            # Check for a detector device (case-insensitive search)
            if "detector" in device_name.lower():
                if value == "1":
                    detector_triggered = True
                    triggered_sensors.append(f"{device_name} at {location}")
            # Check for the alarm system
            if "alarme_system" in device_name.lower():
                if value == "1":
                    alarm_system_on = True
        if detector_triggered and alarm_system_on:
            new_tab = []
            for item in tab:
                parts = [p.strip() for p in item.split(" - ")]
                if len(parts) != 4:
                    new_tab.append(item)
                    continue
                device_name, device_id, location, value = parts
                # Update the alarm (device name contains "alarme" and location is "in_entry")
                if "alarme" in device_name.lower() and location == "in_entry":
                    parts[3] = "1"  # Set the alarm value to 1
                    updated_item = " - ".join(parts)
                    new_tab.append(updated_item)
                else:
                    new_tab.append(item)
            print("Alarm triggered ! ")
            print("Triggered by sensors: " + ", ".join(triggered_sensors) + "\n")
            return new_tab
        else:
            print("No alarm triggered. \n")
            return tab

    


        
