def classify_temperature(celsius):
    if celsius < -20 or celsius > 80:
        raise ValueError("Temperature out of range")

    if celsius < 30:
        return "NORMAL"
    elif celsius < 40:
        return "WARNING"
    else:
        return "CRITICAL"
