import requests
from secret import *

api_address = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f3ae43247b5f4f489a57000e51d11257={key}"
json_data = requests.get(api_address).json()

ar = []

def news(json_data):
    if "articles" in json_data:
        for i in range(3):
            ar.append("number" + str(i + 1) + ": " + json_data["articles"][i]["title"] + ".")
        return ar
    else:
        print("Error: 'articles' key not found in JSON response")
        return ["No news articles found."]

  # For debugging purposes, you can comment this out later
