from check_limits_constants import ideal_state_of_charge_range, ideal_temperature_range, maximum_charge_rate


def check_within_range(value, lower_bound, upper_bound):
    if value < lower_bound or value > upper_bound:
        return False
    return True


def check_battery_status(values, ranges):
    for _value, _range in zip(values, ranges):
        if not check_within_range(_value, *_range):
            return False
    return True


def battery_is_ok(temperature, soc, charge_rate):
    values = [temperature, soc, charge_rate]
    ranges = [
        ideal_temperature_range,
        ideal_state_of_charge_range,
        (0, maximum_charge_rate)
    ]

    if check_battery_status(values, ranges):
        return True
    return False
