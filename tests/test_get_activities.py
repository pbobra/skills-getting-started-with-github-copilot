import pytest


@pytest.mark.asyncio
async def test_get_activities_returns_all_activities(client):
    """Test GET /activities returns all activities with correct structure"""
    # Arrange
    # (activities are pre-populated)
    
    # Act
    response = await client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)


@pytest.mark.asyncio
async def test_get_activities_contains_expected_participants(client):
    """Test that activities include expected participants"""
    # Arrange
    # (activities are pre-populated with test data)
    
    # Act
    response = await client.get("/activities")
    data = response.json()
    
    # Assert
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
