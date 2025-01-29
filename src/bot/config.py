from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from pathlib import Path


env_file = env_file_path = Path(__file__).parent.parent / '.env'


class Settings(BaseSettings):
    TOKEN: SecretStr
    KEY: SecretStr
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8')


settings = Settings()
