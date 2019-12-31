
class Temperature():

    def __init__(self, measure: int):
        self.__set_measure(measure)

    def __set_measure(self, measure):
        self.__check_measure_is_positive(measure)
        self.__measure = measure

    def __check_measure_is_positive(self, measure: int):
        if (measure < 0):
            raise TemperatureNegativeException.from_measure(measure)

    @classmethod
    def take(cls, measure: int):
        return cls(measure)

    def measure(self):
        return self.__measure

    def is_too_hot(self):
        pass


class TemperatureNegativeException(Exception):
    @classmethod
    def from_measure(cls, measure: int):
        return cls(f"Measure should be postive: {measure}")
