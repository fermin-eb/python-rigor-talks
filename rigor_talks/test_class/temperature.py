import os
import sqlite3

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

    def is_super_hot(self) -> bool:
        db_path = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        threshold, = cur.execute("SELECT hot_threshold FROM configuration").fetchone()
        return self.measure() >= threshold


class TemperatureNegativeException(Exception):
    @classmethod
    def from_measure(cls, measure: int):
        return cls(f"Measure should be postive: {measure}")
