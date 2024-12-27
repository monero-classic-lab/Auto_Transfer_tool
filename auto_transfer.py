import requests
import json
import time
import argparse

parser = argparse.ArgumentParser(description='Send transactions to a specified wallet address with varying amounts.')

parser.add_argument('-u', '--wallet_url', type=str, required=True, help='The URL of the wallet RPC server.')
parser.add_argument('-d', '--destination_address', type=str, required=True, help='The destination wallet address.')
parser.add_argument('-t', '--sleep_time', type=int, default=30, help='Time to wait between checks for new block height. Default is 30 seconds.')
parser.add_argument('-a', '--amount', type=float, required=True, help='The amount to send in each transaction.')

args = parser.parse_args()

wallet_url = args.wallet_url
destination_address = args.destination_address
sleep_time = args.sleep_time
amount = args.amount

def send_transaction(destination_address, amount):
    data = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": "transfer",
        "params": {
            "destinations": [
                {"amount": int(amount * 1e11), "address": destination_address}
            ],
            "priority": 0,
            "mixin": 10,
            "ring_size": 11
        }
    }

    headers = {'content-type': 'application/json'}
    response = requests.post(wallet_url, data=json.dumps(data), headers=headers)
    result = response.json()

    print("Transaction response:", result)

def get_block_height():
    data = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": "get_height",
        "params": {}
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(wallet_url, data=json.dumps(data), headers=headers)
    result = response.json()

    if 'result' in result:
        return result['result']['height']
    else:
        print("Error fetching block height")
        return None

last_height = get_block_height()

while True:
    current_height = get_block_height()
    if current_height and last_height and current_height != last_height:
        print(f"New block detected at height {current_height}, sending transaction...")
        send_transaction(destination_address, amount)
        last_height = current_height
    time.sleep(sleep_time)

