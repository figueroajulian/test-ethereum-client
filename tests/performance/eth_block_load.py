
from locust import task, HttpUser, constant_pacing
from clients.blocknumber_client import BlockNumberAsClient
from utils.env_variables import URL


class BlockByNumber(HttpUser):
    block = None

    def get_block(self):
        if self.block is None:
            self.block = BlockNumberAsClient().get_chain_head()
        return self.block

    @task
    def load_block_by_number(self):
        block = self.get_block()
        response = BlockNumberAsClient().get_eth_blockByNumber(block)
        assert response.status_code == 200, "Failed to get block by number"

class Config(HttpUser):
    HttpUser.host = URL
    wait_time = constant_pacing(1)
    tasks = [BlockByNumber]
    total_requests = 10