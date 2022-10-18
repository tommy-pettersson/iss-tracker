import requests

ENDPOINT = "https://api.wheretheiss.at/v1/satellites/25544"

class Networker:
    def get_iss_data():
        try:
            response = requests.get(url=ENDPOINT)
            response.raise_for_status()
        except:
            print("Error getting location data.")
            print(response.text)
        else:
            data = response.json()
            return data
