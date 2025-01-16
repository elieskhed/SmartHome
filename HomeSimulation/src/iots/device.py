from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, house_name, token_house ,device_id, device_name, device_location, device_topic, device_type):
        self._device_id         = device_id
        self._device_name       = device_name
        self._device_location   = device_location
        self._device_topic      = device_topic
        self._device_type       = device_type
        self._house_name        = house_name
        self._house_token       = token_house
        self._device_value      = 0

    @property
    def device_location(self):
        return self._device_location

    @device_location.setter
    def device_location(self, location):
        self._device_location = location

    @property
    def device_name(self):
        return self._device_name

    @property
    def device_id(self):
        return self._device_id
    
    @property
    def device_topic(self):
        return self._device_topic
    
    @property
    def device_type(self):
        return self._device_type
    
    @property
    def house_name(self):
        return self._house_name
    
    @property
    def house_token(self):
        return self._house_token

    @property
    def device_value(self):
        return self._device_value
    
    @device_value.setter
    def device_value(self, value):
        self._device_value = value

    @property
    def device_value(self):
        return self._device_value
    
    @device_value.setter
    def device_value(self, value):
        self._device_value = value

    @abstractmethod
    def convertDataToJSON(self):
        """
        This method should be implemented by all child classes.
        It should return a JSON representation of the device's data.
        """
        pass
    
    @abstractmethod
    def setRandomValue(self):
        """
        This method should be implemented by all child classes.
        It should just modify the value of the sensor
        """
        pass

    def __str__(self):
        return f"device_name: {self.device_name}; device_id: {self.device_id}; device_location: {self.device_location}; device_value: {self.device_value}"
