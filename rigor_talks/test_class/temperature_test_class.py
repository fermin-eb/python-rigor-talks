from rigor_talks.test_class.temperature import Temperature


class TemperatureTestClass(Temperature):

    def get_threshold(self):
        return 50
