from check_limits_constants import ideal_state_of_charge_range, ideal_temperature_range, maximum_charge_rate


def check_within_range(value, lower_bound, upper_bound):
    if value < lower_bound or value > upper_bound:
        return False
    return True

def check_battery_status(values, ranges):
    status = True
    for _value, _range in zip(values, ranges):
        if not check_within_range(_value, *_range):
            return False
    return status


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


if __name__ == '__main__':
    assert (battery_is_ok(25, 70, 0.7) is True)
    assert (battery_is_ok(50, 85, 0) is False)
