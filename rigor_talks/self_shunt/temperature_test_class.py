from rigor_talks.self_shunt.temperature import Temperature


class TemperatureTestClass(Temperature):

    def get_threshold(self):
        return 50
