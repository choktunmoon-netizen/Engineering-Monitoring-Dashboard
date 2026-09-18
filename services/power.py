def calculate_power(voltage: float, current: float) -> float:
    """P = V x I; V > 0, I >= 0; ผิดเงื่อนไข -> ValueError"""
    if voltage <= 0 or current < 0:
        raise ValueError("Voltage ต้องมากกว่า 0 และ Current ต้องมากกว่าหรือเท่ากับ 0")
    return voltage * current

def classify_power(power_watt: float) -> str:
    """คืน NORMAL|WARNING|CRITICAL"""
    if power_watt < 500:
        return "NORMAL"
    elif 500 <= power_watt <= 1000:
        return "WARNING"
    else:
        return "CRITICAL"