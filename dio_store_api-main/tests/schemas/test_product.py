from schemas.product import ProductIn
from tests.factories import product_data


def test_schema_validated():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "IPhone 14"
