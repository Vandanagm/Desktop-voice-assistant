import requests
def get_joke():
    url="http://official-joke-api.appspot.com/random_joke"
    json_data = requests.get(url).json()
    return [json_data["setup"], json_data["punchline"]]
def joke():
    arr = get_joke()
    return arr