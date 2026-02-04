import csv
import os
from datetime import datetime

def save_to_csv(data, filename="air_quality_log.csv"):
    """
    Saves a cleaned data dictionary to a CSV file.
    """
    # Define the headers based on your list
    fieldnames = ["timestamp_checked", "city", "parameter", "value", "unit", "measured_at", "status"]
    
    # Check if the file exists to decide if we need to write the header
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header only once at the start of the file
        if not file_exists:
            writer.writeheader()
        
        # Prepare the row
        writer.writerow({
            "timestamp_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": data["city"],
            "parameter": "pm25",
            "value": data["value"],
            "unit": data["unit"],
            "measured_at": data["timestamp"],
            "status": data.get("status", "N/A") # We'll pass the status from the analyzer
        })