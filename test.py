import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"Healthy" in response.data

def test_get_tasks(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    # Add assertions for the expected response data

def test_add_task(client):
    response = client.post('/api/tasks', json={'title': 'Test Task', 'description': 'A test task'})
    assert response.status_code == 201
    # Add assertions for the expected response data
