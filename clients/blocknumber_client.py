import requests

from utils.env_variables import URL

class BlockNumberAsClient():

    def get_chain_head(self):
        payload = {"method":"eth_blockNumber"
                ,"params":[]}
        response = requests.post(f'{URL}', json=payload)
        response.raise_for_status()
        return response

    def get_eth_blockByNumber(self,block):
        block = block.json()
        hex_number = block['result']
        blockNumber = int(hex_number, 16)
        payload = {
            "method": "eth_getBlockByNumber",
            "params": [blockNumber, True],
            "id": 1,
            "jsonrpc": "2.0"
        }
        response = requests.post(f'{URL}', json=payload)
        response.raise_for_status()
        return response