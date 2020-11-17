import requests


class TestStore:

    def test_create_one_item(self):
        body = {
            'key': 'value',
        }
        URL = 'http://0.0.0.0:8080/keys'
        response = requests.post(URL, json=body)

        assert response.status_code == 201  # created

        response = requests.get(URL)
        assert response.status_code == 200  # OK
        assert response.json()['key'] == 'value'

    def test_delete_all_items(self):
        # create few items
        body = {
            'key': 'value',
            123: 'value1',
        }
        URL = 'http://0.0.0.0:8080/keys'
        requests.post(URL, json=body)

        # delete all
        URL_clear = 'http://0.0.0.0:8080/keys/clear'
        response = requests.post(URL_clear)
        assert response.status_code == 204

        # check
        response = requests.get(URL)
        assert not response.json()

    def test_delete_chosen_items(self):
        # create few items
        body = {
            'key': 'value',
            123: 'value1',
            'key2': 'value2',
        }
        URL = 'http://0.0.0.0:8080/keys'
        requests.post(URL, json=body)

        # delete
        body = [123, 'key2']
        response = requests.delete(URL, json=body)
        assert response.status_code == 204

        # check
        response = requests.get(URL)
        assert response.json()['key'] == 'value'
        assert not response.json().get(123)
        assert not response.json().get('key2')
