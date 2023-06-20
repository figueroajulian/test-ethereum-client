import requests

from assertpy import assert_that
from clients.blocknumber_client import BlockNumberAsClient

# - Testing block chain head
def test_eth_blockNumber():
    eth_blockNumber = BlockNumberAsClient().get_chain_head()

    assert_that(eth_blockNumber.status_code).is_equal_to(requests.codes.ok)

    result = eth_blockNumber.json()
    assert_that(result).contains('result')
    assert isinstance(result['result'], str)

# - Testing block response details
def test_eth_getBlockByNumber():
    block = BlockNumberAsClient().get_chain_head()
    eth_blockByNumber = BlockNumberAsClient().get_eth_blockByNumber(block)

    assert_that(eth_blockByNumber.status_code).is_equal_to(requests.codes.ok)

    result = eth_blockByNumber.json()
    assert_that(result['result']).is_not_empty()
    assert_that(result['hash']).is_not_empty()
    assert_that(result['number']).is_not_empty()
    assert_that(result['author']).is_not_empty()