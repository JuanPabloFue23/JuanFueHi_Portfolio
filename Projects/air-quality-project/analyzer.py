def classify_air_quality(value):
    """
    Categorizes the PM2.5 value based on common health standards.
    """
    if value is None:
        return "Unknown ❓"
    
    if value <= 12.0:
        return "Good ✅"
    elif value <= 35.4:
        return "Moderate ⚠️"
    else:
        return "Unhealthy 🚨"

def generate_report(data):
    """
    Combines data and analysis into a human-readable summary.
    """
    status = classify_air_quality(data['value'])
    print(f"--- 🌬️ Air Quality Report: {data['city']} ---")
    print(f"Status: {status}")
    print(f"Measurement: {data['value']} {data['unit']}")
    print(f"Recorded at: {data['timestamp']}")
    print("-" * 30)