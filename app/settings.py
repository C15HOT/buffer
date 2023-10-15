
import os
from pydantic import BaseSettings


class MongoCollectionsSubSettings(BaseSettings):
    scopus: str = 'videos'


class Settings(BaseSettings):
    mongodb_url: str = os.getenv('MONGODB_URL')
    mongodb_database: str = 'speechup'

    collections: MongoCollectionsSubSettings = MongoCollectionsSubSettings()


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings() -> Settings:
    settings = Settings()
    return settings
