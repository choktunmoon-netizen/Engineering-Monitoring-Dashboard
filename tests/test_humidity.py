import pytest
from services.humidity import classify_humidity


def test_normal():
    assert classify_humidity(50) == "NORMAL"


def test_warning():
    assert classify_humidity(35) == "WARNING"


def test_critical():
    assert classify_humidity(20) == "CRITICAL"


def test_invalid():
    with pytest.raises(ValueError):
        classify_humidity(101)