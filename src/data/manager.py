from .temperature import Temperature
from .state_of_charge import StateOfCharge
from .charge_rate import ChargeRate

class DataManager():
    def __init__(self, data_manager_config):
        self.temperature = Temperature(data_manager_config['temperature_unit'])
        self.state_of_charge = StateOfCharge(data_manager_config["state_of_charge_unit"])
        self.charge_rate = ChargeRate(data_manager_config["charge_rate_unit"])

    def set_values(self,temperature, state_of_charge, charge_rate):
        self.temperature.set_temperature(temperature)
        self.state_of_charge.set_state_of_charge(state_of_charge)
        self.charge_rate.set_charge_rate(charge_rate)

    def get_values(self):
        return {
            "temperature" : self.temperature.value,
            "state_of_charge" : self.state_of_charge.value,
            "charge_rate" : self.charge_rate.value
        }

        