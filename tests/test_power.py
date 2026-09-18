import pytest
from services.power import calculate_power, classify_power

# ทดสอบการคำนวณกำลังไฟฟ้าที่ถูกต้อง
def test_calculate_power_success():
    assert calculate_power(220.0, 2.0) == 440.0
    assert calculate_power(100.0, 0.0) == 0.0

# ทดสอบค่า Voltage หรือ Current ที่ผิดเงื่อนไข
def test_calculate_power_invalid_input():
    with pytest.raises(ValueError):
        calculate_power(0.0, 5.0)  # voltage <= 0
    with pytest.raises(ValueError):
        calculate_power(-10.0, 5.0) # voltage < 0
    with pytest.raises(ValueError):
        calculate_power(220.0, -1.0) # current < 0

# ทดสอบการจำแนกสถานะทั้ง 3 ระดับ
def test_classify_power_normal():
    assert classify_power(499.9) == "NORMAL"

def test_classify_power_warning():
    assert classify_power(500.0) == "WARNING"
    assert classify_power(750.0) == "WARNING"
    assert classify_power(1000.0) == "WARNING"

def test_classify_power_critical():
    assert classify_power(1000.1) == "CRITICAL"