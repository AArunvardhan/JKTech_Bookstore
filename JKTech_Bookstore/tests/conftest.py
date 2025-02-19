import httpx
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from JKTech_Project.JKTech_Bookstore.my_bookstore.main import app
from JKTech_Project.JKTech_Bookstore.my_bookstore.database import get_db
from JKTech_Project.JKTech_Bookstore.my_bookstore.constants import TEST_MONGODB_URI


@pytest.fixture
async def async_client():
    """Fixture for async HTTP client."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client