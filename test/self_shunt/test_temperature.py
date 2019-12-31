import pytest
from unittest import TestCase

from rigor_talks.self_shunt.temperature import (
    Temperature,
    TemperatureNegativeException
)

from rigor_talks.self_shunt.temperature_test_class import TemperatureTestClass


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
            (TemperatureTestClass.take(10)).is_super_hot()
        )

    def test_tryToCheckIfASuperHotTemperatureIsSuperHot(self):
        self.assertTrue(
            (TemperatureTestClass.take(100)).is_super_hot()
        )

    @pytest.mark.skip()
    def test_tryToCheckIfASuperColdTemperatureIsSuperCold(self):
        self.assertTrue(
            (Temperature.take(10)).is_super_cold(None)
        )
