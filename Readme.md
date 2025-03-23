# 🔗 Bitcoin Scripting: Legacy & SegWit Transactions  

## 📌 Project Overview  
This project is part of **CS 216: Introduction to Blockchain** and aims to implement **Bitcoin scripting** for transaction validation using both **Legacy (P2PKH)** and **SegWit (P2SH-P2WPKH)** address formats. The project involves:  

✔️ Setting up a **Bitcoin Core node** in **regtest mode**  
✔️ Creating and executing **Bitcoin transactions** using **Python/C**  
✔️ Understanding **locking (challenge) and unlocking (response) scripts**  
✔️ Analyzing **transaction sizes, script structures, and efficiency**  
✔️ Validating transactions using the **Bitcoin Debugger (`btcdeb`)**  

---

## 🎯 Assignment Objectives  
1. **Legacy Transactions (P2PKH)**  
   - Generate Bitcoin Legacy addresses **A, B, and C**  
   - Create and sign transactions from **A → B** and **B → C**  
   - Extract and analyze the **ScriptPubKey** and **ScriptSig**  
   - Validate transactions using **Bitcoin Debugger**  

2. **SegWit Transactions (P2SH-P2WPKH)**  
   - Generate **SegWit addresses A', B', and C'**  
   - Create and sign transactions from **A' → B' → C'**  
   - Analyze the **witness data** and **segregated signature structure**  
   - Compare **Legacy vs. SegWit** transactions  

3. **Analysis & Comparison**  
   - Measure and compare the **transaction sizes**  
   - Explain the difference between **P2PKH vs. P2SH-P2WPKH scripts**  
   - Evaluate **SegWit efficiency and transaction malleability fixes**  

---

## ⚙️ Tools & Dependencies  
- **Bitcoin Core (bitcoind)** – Full Bitcoin node  
- **Bitcoin CLI (`bitcoin-cli`)** – Command-line interface  
- **Python (`python-bitcoinlib`, `bitcoinrpc`)** – Bitcoin scripting  
- **Bitcoin Debugger (`btcdeb`)** – Script validation  
- **C (`libbitcoin`, `curl` for RPC calls)** – Alternative implementation  

---

## 📥 Setup Instructions  
##  1. Download and Install Bitcoin Core  

### Windows  
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

## 3. Configure bitcoin.conf for Regtest
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

## 5. Run the python script 
```bash
# After starting `bitcoind` and setting up the config, run your Python script
python3 your_script.py
```

## Useful Commands to Verify Bitcoin Node is Running
```
bash
# Check Bitcoin balance
bitcoin-cli -regtest getbalance

# Mine a block
bitcoin-cli -regtest generatetoaddress 1 <your_regtest_address>

# List transactions
bitcoin-cli -regtest listtransactions
```
### Notes
Ensure txindex=1 is set to allow querying transaction details.

Regtest mode is isolated—you must manually generate blocks to process transactions.

Use bitcoin-cli to check balances, transactions, and blocks.

## 🔍 Transaction Execution Workflow
###  Legacy (P2PKH) Transactions
1️⃣ Create three legacy addresses (A, B, C)
2️⃣ Fund Address A using sendtoaddress
3️⃣ Create a raw transaction: A → B
4️⃣ Decode the transaction to extract ScriptPubKey for B
5️⃣ Sign and broadcast the transaction
6️⃣ Create a transaction from B → C, repeat the process
7️⃣ Analyze scripts using Bitcoin Debugger (btcdeb)

## SegWit (P2SH-P2WPKH) Transactions
1️⃣ Create SegWit addresses (A', B', C')
2️⃣ Fund Address A'
3️⃣ Create a raw transaction: A' → B'
4️⃣ Extract witness data and analyze the challenge script
5️⃣ Sign and broadcast the transaction
6️⃣ Create a transaction from B' → C'
7️⃣ Validate SegWit scripts using Bitcoin Debugger



## Team Members
* Ansh Jain (230004005)
* Mahi Shah (230008030)
* Rayavarapu Sreechand (230001068)
* Bhumika Aggarwal (230005011)









