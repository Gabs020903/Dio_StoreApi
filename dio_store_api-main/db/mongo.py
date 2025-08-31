from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


class MongoClient:
    def __init__(self):
        self._client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    @property
    def client(self):
        return self._client


db_client = MongoClient()
