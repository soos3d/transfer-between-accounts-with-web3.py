# Transfer native tokens between accounts using web3.py

This code is the base in web3.py to send tokens between accounts. You can use it to send a token native to a blockchain, such as ETH, AVAX, FTM, etc. 

## Requirements 

To make this code work you will need to have installed:

- [Python](https://www.python.org/downloads/).
- [web3.py library](https://web3py.readthedocs.io/en/stable/quickstart.html)

You can install web3.py with:

```sh
pip install web3
```

> **Note** that on Windows, you will need to install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to make it work.

- Access to a node endpoint, I recommend to use [Chainstack](https://chainstack.com/):

Follow these steps to sign up on Chainstack, deploy a node, and find your endpoint credentials:

  1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).
  1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).
  1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials).

## How to send a transaction

Once you have access to your Chainstack endpoint credentials, you can use it to fill the `node_url` variable. 

> This code was tested on the Fantom testnet, but it will be compatible with all the EMV based networks. 


The first step is to create a new `Python` file, I named it `transfers.py`. 

The first section of the code is to connect to a blockchain.

```py
from web3 import Web3

node_url = "FANTOM_TESTNET_ENDPOINT"  # endpoint URL
web3 = Web3(Web3.HTTPProvider(node_url))  # establish connection to a node
```

> This creates a connection to your node so that you can send and retrieve data.

Then initialize the addresses that you want to use to make the transfer. Don't forget to include the private key from the address used to send the tokens; it is recommended to use an environment variable instead of hardcoding it like in this example!

```py
sender = "SENDER_ADDRESS"
receiver = "RECEIVER_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"
```

Create a `nonce` variable to retrieve the sender address transactions count; this is essential to ensure that the transaction cannot be replayed by someone with malicious intent.

```py
# nonce
nonce = web3.eth.getTransactionCount(sender)
```

We can now estimate the gas limit using the `eth_estimateGas` method, which simulates a transfer between accounts.

```py
# retrieve the gas limit for this simulated transaction.
gas_limit = web3.eth.estimate_gas(({"from":sender,"to":"receiver}), "latest")
#print("The gas limit is:", gas_limit)
```

Then we build the transaction object, where we specify the amount of FTM you want to transfer to the other account. (1 FTM in this example)

```py
tx = {
    "nonce": nonce,
    "to": receiver,
    "value": web3.toWei(1, "ether"),  # measure unit of 1 full token
    "gas": gas_limit,                 # 21000 is good for a simple transfer
    "gasPrice": web3.toWei(10, "gwei"),
    "chainId": web3.eth.chain_id,
}
```

The last step is to sign and send the transaction.

```py
# sign tx
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("Transaction hash:", web3.toHex(tx_hash))
```

This will also print the transaction hash so you can see it on the block explorer😉

Now you only need to run the script and see the magic happens!

```sh
python transfers.py
```
