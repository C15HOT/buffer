from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from app.settings import get_settings

settings = get_settings()

def mongodb_database() -> AsyncIOMotorDatabase:
    return AsyncIOMotorClient(settings.mongodb_url, uuidRepresentation='standard').get_database(settings.mongodb_database)


def scopus_collection() -> AsyncIOMotorCollection:
    return mongodb_database()[settings.collections.scopus]
