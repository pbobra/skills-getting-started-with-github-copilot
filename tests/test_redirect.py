import pytest


@pytest.mark.asyncio
async def test_redirect_to_index(client):
    """Test GET / redirects to /static/index.html"""
    # Arrange
    # (no setup needed)
    
    # Act
    response = await client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
