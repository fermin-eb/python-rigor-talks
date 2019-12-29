from rigor_talks.guard_clauses.temperature import (
    Temperature,
    TemperatureNegativeException
)

from unittest import TestCase


class TestTemperatureTest(TestCase):
    def test_trytoCreateANonValidTemperature(self):
        with self.assertRaises(TemperatureNegativeException):
            Temperature(-1)

    def test_tryToCreateAValidTemperature(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature(measure)).measure()
        )
