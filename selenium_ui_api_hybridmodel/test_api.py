import requests
import pytest

# Example API endpoint
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_posts():
    """Test retrieving all posts from the API."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_create_post():
    """Test creating a new post."""
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201  # Created
    assert response.json()["title"] == "foo"
    assert "id" in response.json()