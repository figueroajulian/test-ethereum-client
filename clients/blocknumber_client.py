import requests

from assertpy import assert_that
from utils.env_variables import URL
from functools import lru_cache

class BlockNumberAsClient():

    @lru_cache(maxsize=None)
    def get_chain_head(self):
        payload = {
            'method':'eth_blockNumber',
            'params':[]
        }
        response = requests.post(f'{URL}', json=payload)
        response.raise_for_status()

        return response

    def get_eth_blockByNumber(self, block):
        block_response = block.json()
        hex_number = block_response['result']
        block_number = int(hex_number, 16)

        payload = {
            "method": "eth_getBlockByNumber",
            "params": [block_number, True],
            "id": 1,
            "jsonrpc": "2.0"
        }
        response = requests.post(f'{URL}', json=payload)
        response.raise_for_status()

        return response