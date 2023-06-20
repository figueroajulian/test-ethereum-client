from locust import task, HttpUser, constant_pacing
from clients.blocknumber_client import BlockNumberAsClient
from utils.env_variables import URL
from locust.exception import StopUser



class BlockByNumber(HttpUser):
    block = None

    def on_start(self):
        if self.block is None:
            self.block = BlockNumberAsClient().get_chain_head()

    @task
    def get_block_by_number(self):
        block = self.block

        block_response = block.json()
        hex_number = block_response['result']
        block_number = int(hex_number, 16)

        payload = {
            "method": "eth_getBlockByNumber",
            "params": [block_number, True],
            "id": 1,
            "jsonrpc": "2.0"
        }

        with self.client.post(f'{URL}', json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to get block by number")

class Config():
    HttpUser.host = URL
    wait_time = constant_pacing(1)
    tasks = [BlockByNumber]