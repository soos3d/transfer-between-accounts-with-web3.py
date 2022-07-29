from web3 import Web3

node_url = "ENDPOINT_URL" #endpoint URL
web3 = Web3(Web3.HTTPProvider(node_url))  # establish connection to a node

# verify the connection is successful (will return true)
if web3.isConnected():
    print("Connection Successful")
else:
    print("Connection Failed")

# initialize the addresses
sender = "SENDER_ADDRESS"
receiver = "RECEIVER_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"

# nonce
nonce = web3.eth.getTransactionCount(sender)

# build the transaction
tx = {
    "nonce": nonce,
    "to": receiver,
    "value": web3.toWei(1, "ether"),  # measure unit of 1 full token
    "gas": 21000,
    "gasPrice": web3.toWei(10, "gwei"),
    "chainId": web3.eth.chain_id,
}

# sign tx
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("Transaction hash:", web3.toHex(tx_hash))
