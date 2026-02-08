import requests

API_KEY = "c5034e04a2e1ca0f557052dcacf967d698f6aa28c740ed64b0995e06fdd6c245"

url = "https://api.openaq.org/v3/locations"

headers = {
    "X-API-Key": API_KEY
}

params = {
    "limit": 10   # number of locations to retrieve
}

response = requests.get(url, headers=headers, params=params)

data = response.json()

# Print locations
for location in data["results"]:
    print(f"ID: {location['id']}")
    print(f"Name: {location['name']}")
    print(f"Country: {location['country']['code']}")
    print(f"Coordinates: {location['coordinates']}")
    print("-----")