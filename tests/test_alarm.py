import pytest
from services.alarm import generate_alarms

def test_all_normal():
    assert generate_alarms("NORMAL", "NORMAL", "NORMAL") == []

def test_single_warning():
    result = generate_alarms("WARNING", "NORMAL", "NORMAL")
    assert result == ["WARNING: Temperature requires attention"]

def test_mixed_warning_critical():
    result = generate_alarms("NORMAL", "CRITICAL", "WARNING")
    assert result == [
        "CRITICAL: Humidity is unsafe",
        "WARNING: Power consumption is high"
    ]

def test_all_critical():
    result = generate_alarms("CRITICAL", "CRITICAL", "CRITICAL")
    assert result == [
        "CRITICAL: Temperature is unsafe",
        "CRITICAL: Humidity is unsafe",
        "CRITICAL: Power consumption is unsafe"
    ]

def test_invalid_input():
    with pytest.raises(ValueError):
        generate_alarms("OK", "NORMAL", "NORMAL")