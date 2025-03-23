
# 🚀 Bitcoin Core Regtest Setup Guide  

This guide will walk you through **installing, configuring, and running** Bitcoin Core in **regtest mode** for local development and testing.  

---

## 📥 1. Download and Install Bitcoin Core  

### 🖥 Windows  
1. Download Bitcoin Core from the [official website](https://bitcoincore.org/en/download/).  
2. Run the installer (`.exe`) and follow the instructions.  
3. Open **Command Prompt** and navigate to the Bitcoin installation directory (`daemon` or `bin` folder).  

### Linux (Ubuntu/Debian)
bash
```
# Step 1: Update package list and install Bitcoin Core
sudo apt update && sudo apt install bitcoin-core

# Step 2: Verify installation
bitcoind --version
```

## 2. Start Bitcoin Daemon in Regtest Mode
```bash
# Start the Bitcoin daemon in regtest mode
bitcoind -regtest
```
This will start the Bitcoin server in regtest mode, allowing for local testing.

##3. Configure bitcoin.conf for Regtest
```bash
# Step 1: Locate the Bitcoin data directory
# Windows: C:\Users\YourUsername\AppData\Roaming\Bitcoin\
# Linux/macOS: ~/.bitcoin/

# Step 2: If `bitcoin.conf` doesn’t exist, create it
touch ~/.bitcoin/bitcoin.conf
```
```ini
# Step 3: Edit `bitcoin.conf` with the following settings
[regtest]
regtest=1
server=1
rpcuser=your_username
rpcpassword=your_password
rpcallowip=127.0.0.1
rpcport=18443
txindex=1
paytxfee=0.0001
fallbackfee=0.0002
mintxfee=0.00001
txconfirmtarget=6
```
⚠️ Note: Replace your_username and your_password with your own values.

## 4. Update Python Script with RPC Credentials
```python
# Update the Python script with RPC credentials from bitcoin.conf
rpc_user = 'your_username'
rpc_password = 'your_password'
rpc_port = 18443

# Example: Connect to Bitcoin RPC using requests
import requests

url = f"http://127.0.0.1:{rpc_port}"
headers = {"content-type": "application/json"}
auth = (rpc_user, rpc_password)

response = requests.get(url, auth=auth)
print(response.json())
```

##5. Run the python script 
```bash
# After starting `bitcoind` and setting up the config, run your Python script
python3 your_script.py
```

##Useful Commands to Verify Bitcoin Node is Running
```
bash
# Check Bitcoin balance
bitcoin-cli -regtest getbalance

# Mine a block
bitcoin-cli -regtest generatetoaddress 1 <your_regtest_address>

# List transactions
bitcoin-cli -regtest listtransactions
```
###Notes
Ensure txindex=1 is set to allow querying transaction details.

Regtest mode is isolated—you must manually generate blocks to process transactions.

Use bitcoin-cli to check balances, transactions, and blocks.










