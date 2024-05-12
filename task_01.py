class AirConditioning:
    def __init__(self, status=False, temperature=None):
        self.__status = status
        self.__temperature = temperature

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if isinstance(new_status, tuple) is True:
            if new_status[1] is True:
                self.__status = new_status[0]

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temperature):
        if isinstance(new_temperature, tuple) is True:
            if new_temperature[1] is True:
                self.__temperature = new_temperature[0]

    def reset(self):
        if self.__status is True:
            self.temperature = (18, True)

    def switch_on(self):
        if self.__status is False:
            self.status = (True, True)
            self.temperature = (18, True)

    def switch_off(self):
        if self.__status is True:
            self.status = (False, True)
            self.temperature = (None, True)

    def get_temperature(self):
        if self.__status is True:
            return self.temperature

    def raise_temperature(self):
        if self.__status is True:
            if self.__temperature < 43:
                self.temperature = (self.__temperature + 1, True)

    def lower_temperature(self):
        if self.__status is True:
            if self.__temperature > 0:
                self.temperature = (self.__temperature - 1, True)

    def __str__(self):
        if self.__status is True:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов.'
        else:
            return f'Кондиционер выключен.'


conditioning = AirConditioning()
print(conditioning)
print(conditioning.temperature)
print(conditioning.status)
conditioning.status = True
print(conditioning)
print(conditioning.status)
conditioning.temperature = 20
print(conditioning.temperature)
conditioning.reset()
print(conditioning)
print(conditioning.get_temperature())
conditioning.raise_temperature()
print(conditioning.get_temperature())
conditioning.lower_temperature()
print(conditioning.get_temperature())
conditioning.switch_on()
print(conditioning)
print(conditioning.get_temperature())
print(conditioning.temperature)
conditioning.temperature = 30
print(conditioning.temperature)
conditioning.status = False
print(conditioning)
for _ in range(16):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(5):
    conditioning.lower_temperature()
print(conditioning.get_temperature())
for _ in range(40):
    conditioning.raise_temperature()
print(conditioning)
for _ in range(5):
    conditioning.raise_temperature()
print(conditioning)
conditioning.switch_off()
print(conditioning)
