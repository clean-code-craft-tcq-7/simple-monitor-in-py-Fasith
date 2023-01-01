class WarningTrigger():
    def __init__(self, trigger_config):
        self.parameter = trigger_config["parameter"]
        self.min_val = trigger_config["min_val"]
        self.max_val = trigger_config["max_val"]
        self.early_warning = trigger_config["early_warning"]
        self.tolerance = trigger_config["tolerance"] * (self.max_val - self.min_val)/100


    def check_for_breach(self,value):
        is_breach = False
        condition = None

        if value > self.max_val:
            is_breach = True
            condition = "High"

        if value < self.min_val:
            is_breach = True
            condition = "Low"

        return {
            "is_breach" : is_breach,
            "condition" : condition
        }


    def check_for_warning(self,value):
        is_warning = False
        condition = None

        if value > self.max_val - self.tolerance and value <= self.max_val:
            is_warning = True
            condition = "High"

        if value < self.min_val + self.tolerance and value >= self.min_val:
            is_warning = True
            condition = "Low"

        return {
            "is_warning" : is_warning,
            "condition" : condition
        }


    # def should_trigger_warning(self, value):
    #     return value > self.max_val or value < self.min_val

    # def should_trigger_early_warning(self, value):
    #     if not self.early_warning:
    #         return False

    #     if self.should_trigger_warning(value):
    #         return False
            
    #     return value > (self.max_val - self.tolerance) \
    #         or value < (self.min_val + self.tolerance)
