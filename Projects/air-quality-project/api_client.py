import requests

def fetch_air_quality(city_name):
    # Using the verified station ID for Madrid
    base_url = "https://api.openaq.org/v3/locations/2178"
    
    headers = {
        "X-API-Key": "c5034e04a2e1ca0f557052dcacf967d698f6aa28c740ed64b0995e06fdd6c245",
        "User-Agent": "PythonAirQualityProject/1.0"
    }
    
    try:
        # We explicitly pass headers to ensure authentication
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None

def process_air_quality_data(raw_data):
    if not raw_data or not raw_data.get("results") or len(raw_data["results"]) == 0:
        return None
    
    # In v3 /latest, we look at the first result in the list
    first_result = raw_data["results"][0]
    
    return {
        "city": "Madrid (Station 2101)",
        "value": first_result.get("value"),
        "unit": "µg/m³",
        "timestamp": first_result.get("datetime", {}).get("utc")
    }
