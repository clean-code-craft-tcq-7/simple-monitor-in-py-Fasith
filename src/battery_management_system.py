from config.parse_config import get_config_from_json
from data.manager import DataManager
from triggers.warning_trigger import WarningTrigger
from logger.base_logger import BaseLogger

class BatteryManagmentSystem():

    def __init__(self, config_path):
        self.data_manager_config, self.logger_config, self.trigger_config_list = \
            get_config_from_json(config_path)

        self.data_manager = DataManager(self.data_manager_config)
        self.triggers = [WarningTrigger(trigger_config) for
                         trigger_config in self.trigger_config_list]

        self.logger = BaseLogger(self.logger_config)
        

    def set_values(self,*args, **kwargs):
        self.data_manager.set_values(*args, **kwargs)

    def check_battery_status(self):
        values = self.data_manager.get_values()
        for trigger in self.triggers:
            value = values[trigger.parameter]

            breach_info = trigger.check_for_breach(value)
            if breach_info["is_breach"]:
                self.logger.log_breach(value, trigger, breach_info["condition"])

            warning_info = trigger.check_for_warning(value)
            if warning_info["is_warning"]:
                self.logger.log_warning(value, trigger, warning_info["condition"])          


if __name__ == "__main__":
    bms = BatteryManagmentSystem("./config/data/default_config.json")
    bms.set_values(100,21,0.70)
    bms.check_battery_status()