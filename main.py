import requests
import os

BASE_URL = "https://developer.sepush.co.za/business/2.0"

class LoadShedding:
    '''
    Create a new instance of the Eskom Load Shedding class.

    Args:
        area_id (str): The identifier for the specific area.
        api_key (str): Your API key for the Eskom API.
        base_url (str): The base URL for the API (optional).
    '''

    def __init__(self, area_id, api_key=None, base_url=None):
        self.api_key = api_key or os.environ.get('ESKOMSEPUSH')
        self.area_id = area_id
        self.base_url = base_url or os.environ.get('BASE_URL_ESKOM') or BASE_URL
        self.headers = {'Token': self.api_key}

    def make_request(self, endpoint, payload=None):
        '''Used to make a request to the Eskom API endpoint.'''
        query_url = self.base_url + endpoint
        try:
            response = requests.get(url=query_url, headers=self.headers, params=payload)
            response.raise_for_status()  # Raise an error for non-2xx response codes

            return response.json()

        except requests.RequestException as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    area_id = "eersteriver"  # Make sure to define area_id as a string
    app = LoadShedding(area_id)
    data = app.make_request("/status")  # Use the relative endpoint path
    if data:
        print(data)



