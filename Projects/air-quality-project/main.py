import time
from api_client import fetch_air_quality, process_air_quality_data
from analyzer import classify_air_quality, generate_report

def run_guardian(city):
    print(f"🚀 Starting Air Quality Guardian for {city}...")
    
    # 1. Fetch
    raw_response = fetch_air_quality(city)
    
    # 2. Process
    clean_data = process_air_quality_data(raw_response)
    
    if clean_data:
        # 3. Analyze & Report
        generate_report(clean_data)
    else:
        print("❌ Could not complete the analysis.")

if __name__ == "__main__":
    # For now, we run it once. Later we can add the loop!
    target_city = "Madrid" 
    run_guardian(target_city)