import os
import dotenv
import requests
from service.flight_search import FlightSearch

dotenv.load_dotenv(dotenv.find_dotenv())
END_POINT = os.environ.get("URL_SHEETY")
API_KEY = os.environ.get("API_SHEETY")
headers = {
    "Authorization": f"Bearer {API_KEY}"
}


class DataManager:
    def __init__(self):
        self.cities = []
        self.iata_codes = []
        self.lowest_prices = []
        self.get_cities()
        self.post_iata_codes()

    def get_cities(self):
        response = requests.get(url=END_POINT, headers=headers)
        data = response.json().get("prices")
        self.lowest_prices = [data[x].get("lowestPrice") for x in range(len(data))]
        self.cities = [data[x].get("city") for x in range(len(data))]

    def post_iata_codes(self):
        flight_search = FlightSearch()
        self.iata_codes = [flight_search.iata_codes(city=city) for city in self.cities]
        row = 2
        for code in self.iata_codes:
            iata = {"price":
                        {
                            'iataCode': code,
                            'id': row
                        }
                    }
            res = requests.put(url=END_POINT+f"/{row}", json=iata, headers=headers)
            row += 1

    def get_information(self):
        response = requests.get(url=END_POINT, headers=headers)
        data = response.json()['prices']
        return data
