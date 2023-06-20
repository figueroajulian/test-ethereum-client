import requests

from assertpy import assert_that
from clients.blocknumber_client import BlockNumberAsClient
from utils.env_variables import URL

def test_eth_blockNumber():
    # Get the block number
    eth_blockNumber = BlockNumberAsClient().get_chain_head()

    # Verify that the request was successful
    assert_that(eth_blockNumber.status_code).is_equal_to(requests.codes.ok)

    # Verify the response content
    block = eth_blockNumber.json()
    assert_that(block).described_as("Invalid response").contains_entry({"jsonrpc": "2.0"})
    assert_that(block['result']).is_not_none()


def test_eth_getBlockByNumber():
    # Get the first block
    firstBlock = BlockNumberAsClient().get_chain_head()

    # Get the block details by block number
    eth_blockByNumber = BlockNumberAsClient().get_eth_blockByNumber(firstBlock)

    # Verify that the request was successful
    assert_that(eth_blockByNumber.status_code).is_equal_to(requests.codes.ok)

    # Verify the response content
    blockDetails = eth_blockByNumber.json()['result']
    assert_that(blockDetails).contains_key('hash')
    assert_that(blockDetails).contains_key('number')
    assert_that(blockDetails).contains_key('hash')
    assert_that(blockDetails['gasUsed']).is_type_of(str).matches(r'^0x[0-9a-fA-F]+$')
    assert_that(blockDetails['difficulty']).is_instance_of(str)