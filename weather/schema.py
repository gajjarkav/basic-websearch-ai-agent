from pydantic import BaseModel


class get_weather_schema(BaseModel):
    location: str