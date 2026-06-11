def celsius_to_fahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2)

def test_freezing():
    assert celsius_to_fahrenheit(0) == 32.0

def test_boiling():
    assert celsius_to_fahrenheit(100) == 212.0

def test_negative():
    assert celsius_to_fahrenheit(-40) == -40.0

def test_body_temp():
    assert celsius_to_fahrenheit(37) == 98.6