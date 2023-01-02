import logging


class BaseLogger():

    def __init__(self, logger_config) -> None:
        self.logger = logging
        self.language = logger_config["language"]
        log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
            "%(filename)s::%(lineno)d::%(message)s"

        log_format = "%(levelname)s::%(message)s"

        self.logger.basicConfig(level='DEBUG', format=log_format)

    def log_breach(self, value, trigger, condition):

        if self.language == "english":
            status = {
                "High": "above",
                "Low": "below"
            }
            log_string = f"Threshold breach! \n"
            log_string += f"{trigger.parameter} is {status[condition]} threshold. \n"
            log_string += f"Current value {value}. Expected range: ({trigger.min_val}, {trigger.max_val})\n"
            self.logger.critical(log_string)

        elif self.language == "german":
            status = {
                "High": "über",
                "Low": "unter"
            }
            log_string = f"Schwellenbruch! \n"
            log_string += f"{trigger.parameter} liegt {status[condition]} dem Schwellenwert. \n"
            log_string += f"Aktueller Wert {value}. Erwarteter Bereich: ({trigger.min_val}, {trigger.max_val}) \n"
            self.logger.critical(log_string)

    def log_warning(self, value, trigger, condition):

        if self.language == "english":
            status = {
                "High": "Upper",
                "Low": "Lower"
            }
            log_string = f"Warning - reaching threshold! \n"
            log_string += f"{trigger.parameter} is approaching {status[condition]} threshold limit. \n"
            log_string += f"Current value {value}. Expected range: ({trigger.min_val}, {trigger.max_val})\n"
            self.logger.warning(log_string)

        elif self.language == "german":
            status = {
                "High": "oberen",
                "Low": "unteren"
            }
            log_string = f"Achtung - Schwellenwert erreicht! \n"
            log_string += f"{trigger.parameter} nähert sich dem {status[condition]} Schwellenwert. \n"
            log_string += f"Aktueller Wert {value}. Erwarteter Bereich: ({trigger.min_val}, {trigger.max_val}) \n"
            self.logger.warning(log_string)
