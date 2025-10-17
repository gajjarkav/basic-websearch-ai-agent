from langchain_community.tools import tool
from weather.schema import get_weather_schema
from setting import settings
import requests

@tool(args_schema=get_weather_schema)
def get_weather(location: str) -> str:
    """
    use this tool to get weather info
    """
    # here i use openweather base url you can change according as what service provider you use
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    api_key = settings.OPENWEATHER_API_KEY
    if not api_key:
        return "Error: OpenWeatherMap API key is not set in the environment variables."

    params = {
        "q" : location.strip().lower(),
        "appid" : api_key,
        "units" : "metric"      #this shows weather in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (
            f"The current weather in {location.title()} is {weather_desc}. "
            f"The temperature is {temp}°C, but it feels like {feels_like}°C. "
            f"Humidity is at {humidity}%, and the wind speed is {wind_speed} m/s."
        )

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return f"Sorry, I couldn't find the city '{location}'. Please check the spelling."
        else:
            return f"An HTTP error occurred: {http_err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"