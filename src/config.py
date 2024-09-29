from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str

    # specify where we are getting our...
    # .env settings from.
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


# we are going to be importing this...
# whenever we require an environment variable.
Config = Settings()