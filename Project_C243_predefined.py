#import the Web3 module from Web3 library
from web3 import Web3
from web3.middleware import geth_poa_middleware

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

latest_block = web3.eth.getBlock('latest')
print("Latest Block of ethereum blockchain: ",latest_block)

block_transaction_count = web3.eth.get_block_transaction_count(16495367)
print("Number of transactions happend in the block",block_transaction_count)

transaction_fee = web3.eth.fee_history(9,'latest',None)
print("Number of transactions happend in the block",transaction_fee)