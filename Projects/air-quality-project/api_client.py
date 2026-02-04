import requests

def fetch_air_quality(city_name):
    """
    Fetches the latest PM2.5 measurements for a given city.
    """
    base_url = "https://api.openaq.org/v2/measurements"
    
    # These parameters filter the data so we only get what we need
    params = {
        "city": city_name,
        "parameter": "pm25",
        "limit": 1,        # Just get the most recent one
        "order_by": "datetime"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        # This checks if the HTTP request was successful (Status Code 200)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None