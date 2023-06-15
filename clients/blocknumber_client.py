import requests

from utils.env_variables import URL

class BlockNumberAsClient():

    def get_chain_head():
        params = {"method":"eth_blockNumber"
                ,"params":[]}
        response = requests.post(f'{URL}', params=params)
        response.raise_for_status()
        return response.json()