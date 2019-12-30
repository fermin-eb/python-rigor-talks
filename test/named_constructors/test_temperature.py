from unittest import TestCase

from rigor_talks.named_constructors.temperature import (
    Temperature,
    TemperatureNegativeException
)


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

    def test_trytoCreateAValidTemperatureWithNamedConstructor(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature.take(measure)).measure()
        )
