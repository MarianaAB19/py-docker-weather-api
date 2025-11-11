import os
import requests


api_url = "http://api.weatherapi.com/v1/current.json"
city = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    try:
        result = requests.get(api_url, params={"key": api_key, "q": city})
        result.raise_for_status()
    except requests.RequestException as exc:
        print(f"Error: {exc}")
        return
    data = result.json()
    print(
        f"Weather in {city}, "
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
