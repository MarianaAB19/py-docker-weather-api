import os
import requests


def get_weather() -> None:
    API_URL = "http://api.weatherapi.com/v1/current.json"
    CITY = "Paris"
    API_KEY = os.getenv("API_KEY")
    result = requests.get(API_URL, params={"key": API_KEY, "q": CITY})
    data = result.json()
    print(
        f"Weather in {CITY}, "
        f"{data.get('location').get('country')} "
        f"{data.get('current').get('last_updated')}"
    )
    print(f"Condition: {data.get('current').get('condition').get('text')}")
    print(f"Temperature: {data.get('current').get('temp_c')} °C")
    print(f"Wind: {data.get('current').get('wind_kph')} km/h")
    print(f"Humidity: {data.get('current').get('humidity')} %")
    print(f"Cloud: {data.get('current').get('cloud')} %")


if __name__ == "__main__":
    get_weather()
