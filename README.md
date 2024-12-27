# XMC Auto Transfer Tool

This Python script allows you to send transactions to a specified wallet address using a wallet RPC server. It continuously monitors the block height and sends transactions with a specified amount whenever a new block is detected. The transaction amount is provided through a command-line argument, and the time between block height checks can also be customized.

## Prerequisites

Before running this script, ensure that you have the following dependencies installed:

- Python 3.x
- `requests` library (for making HTTP requests to the wallet RPC server)

You can install the required library using pip:

```bash
pip install requests
```

## Usage
To run the script, you need to provide the following command-line arguments:

* `-u` or `--wallet_url`: The URL of the wallet RPC server.
* `-d` or `--destination_address`: The destination wallet address to send the transaction to.
* `-a` or `--amount`: The amount (in Monero-Classic units) to send in each transaction.
* `-t` or `--sleep_time`: Optional. The time (in seconds) to wait between checks for the new block height. Default is 30 seconds.

## Example
To send a transaction of 2.5 XMC to a specified wallet address every time a new block is detected, you would run:

```bash
python auto_transfer.py -u <wallet_url> -d <destination_address> -a 2.5 -t 30
```

## How It Works
1. The script starts by fetching the current block height from the specified wallet RPC server.
2. It then enters a loop that periodically checks for new block heights.
3. Each time a new block is detected (i.e., the current block height differs from the last checked block height), the script sends a transaction with the specified amount to the destination wallet address.
4. The time between block height checks can be adjusted via the -t argument (default is 30 seconds).
5. The amount sent in each transaction is the one specified by the -a argument.


## Customization
* You can modify the sleep_time argument to control how often the script checks the block height.
* The script currently sends the same amount each time a new block is detected. You can customize the transaction logic if you want to implement more complex behavior (such as changing the amount based on block height).

## License
This script is provided as-is, free of charge. Use it at your own risk.
