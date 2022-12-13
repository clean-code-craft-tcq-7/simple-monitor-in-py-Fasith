from check_limits_constants import ideal_state_of_charge_range, ideal_temperature_range, maximum_charge_rate


def check_within_of_range(value, lower_bound, upper_bound):
    if value < lower_bound or value > upper_bound:
        return False
    return True


def battery_is_ok(temperature, soc, charge_rate):
    if not check_within_of_range(temperature, *ideal_temperature_range):
        return False
    if not check_within_of_range(soc, *ideal_state_of_charge_range):
        return False
    if charge_rate > maximum_charge_rate:
        return False
    return True



if __name__ == '__main__':
    assert (battery_is_ok(25, 70, 0.7) is True)
    assert (battery_is_ok(50, 85, 0) is False)
