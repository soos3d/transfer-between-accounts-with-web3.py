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

## Test the script

Once you have access to your Chainstack endpoint credentials, you can use it to fill the `node_url` variable. 

> This code was tested on the Fantom testnet, but it will be compatible with all the EMV based networks. 

```py
from web3 import Web3

node_url = "FANTOM_TESTNET_ENDPOINT"  # endpoint URL
web3 = Web3(Web3.HTTPProvider(node_url))  # establish connection to a node
```

Then customize the addresses that you want to use to make the transfer. Don't forget to include the private key from the address used to send the tokens; it is recommended to use an environment variable instead of hardcoding it like in this example!

```py
sender = "SENDER_ADDRESS"
receiver = "RECEIVER_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"
```

Then specify the amount of FTM that you want to transfer to the other account. (1 FTM in this example)

```py
tx = {
    "nonce": nonce,
    "to": receiver,
    "value": web3.toWei(1, "ether"),  # measure unit of 1 full token
    "gas": 21000,
    "gasPrice": web3.toWei(10, "gwei"),
    "chainId": web3.eth.chain_id,
}
```

Now you only need to run the script and see the magic happens! It will also print the transaction hash in the console😉
