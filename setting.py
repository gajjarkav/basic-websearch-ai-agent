from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr
from typing import Optional

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    GROQ_API_KEY: Optional[str] = None
    OPENROUTER_API_KEY: Optional[str] = None
    GROQ_LLM_MODEL: Optional[str] = None
    OPENROUTER_LLM_MODEL: Optional[str] = None
    TEMPERATURE: float = 0.0

#   here i am using openweather attach api key in .env file
    OPENWEATHER_API_KEY: Optional[str] = None

settings = Settings()
