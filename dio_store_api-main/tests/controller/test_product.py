import pytest
from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    response.json()

    assert response.status_code == status.HTTP_201_CREATED


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}1eee3f99-3d20-4112-ad69-d86672a5d7cf")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 1eee3f99-3d20-4112-ad69-d86672a5d7cf"
    }


@pytest.mark.usefixtures("product_inserted")
async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"quantity": 40}
    )

    assert response.status_code == status.HTTP_200_OK


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}1eee3f99-3d20-4112-ad69-d86672a5d7cf"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 1eee3f99-3d20-4112-ad69-d86672a5d7cf"
    }
