from service.flight_search import FlightSearch
from service.data_manager import DataManager
import datetime as dt
from service.notification_manager import send_email

sheety_data = DataManager()
data = sheety_data.get_information()

flight_search = FlightSearch()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
future = dt.datetime.now() + dt.timedelta(days=90)
future = future.strftime("%d/%m/%Y")

for idx in range(len(data)):

    deal_parameters = {
        "fly_from": "MAD",
        "fly_to": data[idx]['iataCode'],
        "date_from": tomorrow,
        "date_to": future,
        "nights_in_dst_from": 10,
        "nights_in_dst_to": 15,
        "flight_type": 'round',
        "curr": "EUR",
        "max_stopovers": 0

    }

    deals = flight_search.deal_finder(deal_parameters)
    if len(deals["data"]) > 1:
        deal_price = deals["data"][0]["price"]
        if deal_price <= data[idx]["lowestPrice"]:
            origin = deals["data"][0]["cityFrom"]
            origin_iata = deals["data"][0]["flyFrom"]
            destination = deals["data"][0]["cityTo"]
            destination_iata = deals["data"][0]["flyTo"]
            link = deals["data"][0]["deep_link"].replace("&affilid=kevsdedealfinder", "")
            departure = deals["data"][0]["route"][0]["local_departure"].split("T")[0]
            return_home = deals["data"][0]["route"][1]["local_departure"].split("T")[0]
            nights = deals["data"][0]["nightsInDest"]
            message = f"Subject:New Deal\n\nLow price alert! {nights} nights Only {deal_price}€ " \
                      f"to fly from {origin}-{origin_iata} to {destination}-{destination_iata}, " \
                      f"from {departure} to {return_home} \nlink: {link}"
            message = message.encode("utf8")
            send_email(message)
