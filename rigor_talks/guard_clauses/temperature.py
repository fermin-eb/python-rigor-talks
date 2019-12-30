
class TemperatureNegativeException(Exception):
    pass


class Temperature():

    def __init__(self, measure: int):
        # Guard clause: simplify code and raise exceptions
        # Passed guard clauses, code is valide
        self._check_measure_is_positive(measure)

        self.__measure = measure

    def _check_measure_is_positive(self, measure: int):
        if (measure < 0):
            raise TemperatureNegativeException("Measure should be postive")

    def measure(self):
        return self.__measure
