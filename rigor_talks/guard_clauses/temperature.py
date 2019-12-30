
class TemperatureNegativeException(Exception):
    pass


class Temperature():

    def __init__(self, measure: int):
        self.__set_measure(measure)

    def __set_measure(self, measure):
        self.__check_measure_is_positive(measure)
        self.__measure = measure

    def __check_measure_is_positive(self, measure: int):
        if (measure < 0):
            raise TemperatureNegativeException("Measure should be postive")

    def measure(self):
        return self.__measure
