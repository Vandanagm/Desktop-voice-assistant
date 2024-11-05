import requests
from secret import *

# Form the correct API address with the API key
api_address = f'http://api.openweathermap.org/data/2.5/weather?q=bengaluru&appid={key2}'

# Make the request to the API
response = requests.get(api_address)

# Check if the request was successful
if response.status_code == 200:
    json_data = response.json()
     # Print the entire JSON response for debugging

    def temp():
        if "main" in json_data:
            temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Using 273.15 for accurate Celsius conversion
            return temperature
        else:
            return "Temperature data not available"

    def des():
        if "weather" in json_data and len(json_data["weather"]) > 0:
            description = json_data["weather"][0]["description"]
            return description
        else:
            return "Weather description not available"

