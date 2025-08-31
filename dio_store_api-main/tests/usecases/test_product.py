from typing import List
from uuid import UUID

import pytest
from core.exceptions import NotFoundException
from schemas.product import ProductOut, ProductUpdateOut
from usecases.product import usecase


async def test_usecase_create_should_return_success(product_in):
    result = await usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "IPhone 14"


async def test_usecase_get_should_return_success(product_inserted):
    result = await usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "IPhone 14"


async def test_usecase_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await usecase.get(id=UUID("0833f163-8c2a-4066-9a0f-b0620de76d8a"))

    assert (
        err.value.message
        == "Product not found with filter: 0833f163-8c2a-4066-9a0f-b0620de76d8a"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecase_query_should_return_success():
    result = await usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecase_update_should_return_success(product_up, product_inserted):
    product_up.price = 5000.0
    result = await usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecase_delete_should_return_success(product_inserted):
    result = await usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecase_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await usecase.delete(id=UUID("0833f163-8c2a-4066-9a0f-b0620de76d8a"))

    assert (
        err.value.message
        == "Product not found with filter: 0833f163-8c2a-4066-9a0f-b0620de76d8a"
    )
