import httpx
import pytest
from httpx import AsyncClient
# from JKTech_Project.JKTech_Bookstore.my_bookstore.main import app


@pytest.mark.asyncio
async def test_create_and_get_book(async_client: AsyncClient):
    # Create a book
    create_response = await async_client.post(
        "/books",
        json={"title": "Test Book", "author": "Test Author", "year": 2023}
    )
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    # Retrieve the book
    get_response = await async_client.get(f"/books/{book_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Test Book"
