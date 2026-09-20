def classify_humidity(percent: float) -> str:

    # นอกช่วง 0-100
    if percent < 0 or percent > 100:
        raise ValueError("Humidity must be between 0 and 100")

    # 40-60 = NORMAL
    if 40 <= percent <= 60:
        return "NORMAL"

    # 30-39 และ 61-70 = WARNING
    if 30 <= percent < 40 or 60 < percent <= 70:
        return "WARNING"

    # <30 และ >70 = CRITICAL
    return "CRITICAL"