from check_limits import battery_is_ok

def test_battery_is_okay():
    assert (battery_is_ok(25, 70, 0.7) is True)
    assert (battery_is_ok(50, 85, 0) is False)