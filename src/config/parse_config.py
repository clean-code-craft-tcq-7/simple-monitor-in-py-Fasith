import pathlib
import json

# from .model import WarningTriggerConfig, DataManagerConfig, LoggerConfig


def parse_trigger_config(parameter, trigger_config):
    parsed_config = {}
    parsed_config["parameter"] = parameter
    parsed_config["min_val"] = trigger_config["minimum_value"]
    parsed_config["max_val"] = trigger_config["maximum_value"]
    parsed_config["early_warning"] = trigger_config["early_warning_enabled"]
    parsed_config["tolerance"] = trigger_config["early_warning_tolerance_percentage"]
    return parsed_config


def parse_data_manager_config(data_manager_config):
    return data_manager_config


def parse_logger_config(logger_config):
    return logger_config


def get_config_from_json(filepath: pathlib.Path):

    with open(filepath) as file:
        config_data = json.load(file)
        parsed_data_manager_config = parse_data_manager_config(
            config_data["data_manager"])
        parsed_logger_config = parse_logger_config(config_data["logger"])
        parsed_trigger_config_list = []
        for parameter, trigger_config in config_data["triggers"].items():
            parsed_trigger_config = parse_trigger_config(parameter, trigger_config)
            parsed_trigger_config_list.append(parsed_trigger_config)

    return parsed_data_manager_config, parsed_logger_config, parsed_trigger_config_list


if __name__ == "__main__":
    x,y,z = get_config_from_json("/home/fak2kor/Desktop/TCQ/simple-monitor-in-py-Fasith/src/config/data/default_config.json")
    print(x)
    print(y)
    print(z)