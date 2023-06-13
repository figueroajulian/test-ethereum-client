
from clients.base_client import BaseClient
from utils.env_variables import URL

class BlockNumberAsClient(BaseClient):
    def __init__(self, user_token=None):
        super().__init__(user_token)
        self.endpoint = f'{URL}'

    def get_chain_head():
        pass