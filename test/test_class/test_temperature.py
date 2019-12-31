from unittest import TestCase

from rigor_talks.test_class.temperature import (
    Temperature,
    TemperatureNegativeException
)


class TestTemperatureTest(TestCase):

    def test_trytoCreateANonValidTemperature(self):
        with self.assertRaises(TemperatureNegativeException):
            Temperature.take(-1)

    def test_tryToCreateAValidTemperature(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature.take(measure)).measure()
        )

    def test_trytoCreateAValidTemperatureWithNamedConstructor(self):
        measure = 18
        self.assertEqual(
            measure,
            (Temperature.take(measure)).measure()
        )

    def test_tryToCheckIfAColdTemperatureIsSuperHot(self):
        self.assertFalse(
            (Temperature.take(10)).is_super_hot()
        )

    def test_tryToCheckIfASuperHotTemperatureIsSuperHot(self):
        self.assertTrue(
            (Temperature.take(100)).is_super_hot()
        )
