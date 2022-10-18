from datetime import datetime
from networker import Networker

class DataManager:
    
    def get_iss_location():
        
        data = Networker.get_iss_data()

        time = datetime.fromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M")

        new_data = {
            "id": data["id"],
            "time": time,
            "latitude": data["latitude"],
            "longitude": data["longitude"]
        }

        return new_data
