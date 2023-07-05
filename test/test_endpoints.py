import os
import requests

def test_blueprint_user(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'user')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'name' in json
    assert 'image' in json