import requests
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
API_KEY = os.environ.get("API_TEQUILA")
headers = {
    "apikey": API_KEY
}
URL = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    def deal_finder(self, parameters: dict):
        response = requests.get(url=URL, params=parameters, headers=headers)
        return response.json()

    def iata_codes(self, city):
        country_parameters = {
            "term": city
        }
        res = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=country_parameters, headers=headers)
        return res.json().get("locations")[0].get("code")


