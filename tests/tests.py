import requests


class TestStore:

    def test_create_one_item(self):
        body = {
            'key': 'value',
        }
        URL = 'http://0.0.0.0:8080/keys'
        requests.post(URL, json=body)

        response = requests.get(URL)
        assert response.json()['key'] == 'value'
