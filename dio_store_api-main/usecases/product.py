from uuid import UUID
import uuid
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from core.exceptions import NotFoundException
from db.mongo import db_client
from models.product import ProductModel
from schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUsecase:
    def __init__(self):
        self.client: AsyncIOMotorClient = db_client.client
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn):
        product_model = ProductModel(**body.model_dump())
        product = ProductOut(**product_model.model_dump())

        product_dict = product_model.model_dump()
        if isinstance(product_dict.get("id"), uuid.UUID):
            product_dict["id"] = str(product_dict["id"])

        await self.collection.insert_one(product_dict)

        return product

    async def get(self, id: UUID):
        id = str(id)
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(self):
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate):
        id = str(id)
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID):
        id = str(id)
        product = await self.collection.find_one({"id": id})

        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


usecase = ProductUsecase()
