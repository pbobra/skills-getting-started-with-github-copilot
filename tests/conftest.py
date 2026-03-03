import pytest
import pytest_asyncio
import copy
from httpx import AsyncClient, ASGITransport
from src.app import app, activities


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test."""
    initial_state = copy.deepcopy(activities)
    yield
    # Restore state after test
    activities.clear()
    activities.update(initial_state)


@pytest_asyncio.fixture
async def client(reset_activities):
    """Provide an async test client."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
