import requests

class BaseClient:
    def __init__(self, user_token=None):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': user_token
        }
        self.request = requests
