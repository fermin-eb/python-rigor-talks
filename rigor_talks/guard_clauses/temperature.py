
class TemperatureNegativeException(Exception):
    pass


class Temperature():

    def __init__(self, measure: int):
        if (measure < 0):
            raise TemperatureNegativeException("Measure should be postive")

        self.__measure = measure

    def measure(self):
        return self.__measure
