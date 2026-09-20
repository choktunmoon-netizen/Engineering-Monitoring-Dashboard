# services/alarm.py
def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str
) -> list[str]:
    """คืน list ข้อความเตือน; ถ้าปกติทั้งหมดคืน []"""
    valid_statuses = {"NORMAL", "WARNING", "CRITICAL"}
    
    if temp_status not in valid_statuses or humid_status not in valid_statuses or power_status not in valid_statuses:
        raise ValueError("สถานะไม่ถูกต้อง ต้องเป็น NORMAL, WARNING หรือ CRITICAL เท่านั้น")
        
    alarms = []
    
    # Temperature 
    if temp_status == "WARNING":
        alarms.append("WARNING: Temperature requires attention")
    elif temp_status == "CRITICAL":
        alarms.append("CRITICAL: Temperature is unsafe")
        
    # Humidity
    if humid_status == "WARNING":
        alarms.append("WARNING: Humidity requires attention")
    elif humid_status == "CRITICAL":
        alarms.append("CRITICAL: Humidity is unsafe")
        
    # Power
    if power_status == "WARNING":
        alarms.append("WARNING: Power consumption is high")
    elif power_status == "CRITICAL":
        alarms.append("CRITICAL: Power consumption is unsafe")
        
    return alarms