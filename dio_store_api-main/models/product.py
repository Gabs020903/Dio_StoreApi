from models.base import CreateBaseModel
from schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    pass
