class WarningTrigger():
    def __init__(self, trigger_config):
        self.parameter = trigger_config["parameter"]
        self.min_val = trigger_config["min_val"]
        self.max_val = trigger_config["max_val"]
        self.early_warning = trigger_config["early_warning"]
        self.tolerance = trigger_config["tolerance"] * (self.max_val - self.min_val)/100


    def _check_if_outside_limits(self,value, lower_bound , upper_bound):
        is_outside_limits = False
        condition = None
        if value > upper_bound:
            is_outside_limits = True
            condition = "High"
        
        if value < lower_bound:
            is_outside_limits = True
            condition = "Low"

        return {
            "is_outside_limits" : is_outside_limits,
            "condition": condition
        }


    def check_for_breach(self,value):
        
        breach_status = self._check_if_outside_limits(value, self.min_val, self.max_val)
        return {
            "is_breach" : breach_status["is_outside_limits"],
            "condition" : breach_status["condition"]
        }


    def check_for_warning(self,value):
        warning_status = self._check_if_outside_limits(value, self.min_val + self.tolerance, self.max_val - self.tolerance)

        if  warning_status["is_outside_limits"]:            
            is_breach = self.check_for_breach(value)["is_breach"]
            if not is_breach:
                return {
                    "is_warning" : warning_status["is_outside_limits"],
                    "condition" : warning_status["condition"]
                }

        return {
            "is_warning" : False,
            "condition" : None
        }
