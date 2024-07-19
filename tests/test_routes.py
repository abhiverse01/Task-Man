def test_create_task(client):
    response = client.post('/api/tasks', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Test Task'

def test_get_tasks(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
