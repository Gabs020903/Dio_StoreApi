from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, Field, PositiveFloat, PositiveInt
from schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product's name")
    quantity: PositiveInt = Field(..., description="Product's quantity")
    price: PositiveFloat = Field(..., description="Product's price")
    status: bool = Field(..., description="Product's status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[PositiveInt] = Field(None, description="Product's quantity")
    price: Optional[PositiveFloat] = Field(None, description="Product's price")
    status: Optional[bool] = Field(None, description="Product's status")


class ProductUpdateOut(ProductOut):
    ...
