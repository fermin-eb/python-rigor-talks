
class TemperatureNegativeException(Exception):
    pass


class Temperature():

    def __init__(self, measure: int):
        if (measure >= 0):
            self.__measure = measure
        else:
            raise TemperatureNegativeException("Measure should be postive")

    def measure(self):
        return self.__measure
