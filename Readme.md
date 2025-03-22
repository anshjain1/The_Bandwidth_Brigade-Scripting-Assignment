## 🔧 Setup Instructions

###  1. Start Bitcoin Daemon (bitcoind) in regtest mode
- Open Command Prompt (or Terminal)
- Navigate to the Bitcoin Core installation directory (`daemon` or `bin` folder)
- Run the following command:
```bash
bitcoind -regtest
```
- This will start the Bitcoin server in regtest mode.

---

###  2. Configure `bitcoin.conf` for regtest
- Go to the **regtest folder** where `bitcoin.conf` is located. (Usually in `~/.bitcoin/regtest/` or `AppData\Roaming\Bitcoin\regtest`)
- Edit `bitcoin.conf` with the following content:
```
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
⚠️ **Note:** Replace `your_username` and `your_password` with your own values.

---

###  3. Update Python Script with RPC Credentials
- Open the Python program (the script that interacts with the Bitcoin node).
- Make sure you update the **RPC credentials** in your Python script to match the ones set in `bitcoin.conf`:
```python
rpc_user = 'your_username'
rpc_password = 'your_password'
rpc_port = 18443
```

---

###  4. Run the Python Script
- After starting `bitcoind` and setting up the config, run your Python script to execute the transactions:
```bash
python3 your_script.py
```

---

##  Important Notes:
- Ensure `txindex=1` is set to allow querying transaction details.
- `regtest` mode is isolated; you control mining and block generation.
- Use the `bitcoin-cli` tool to check balances, transactions, and blocks.

---

## 💻 Useful Commands
Check balance:
```bash
bitcoin-cli -regtest getbalance
```

Mine a block:
```bash
bitcoin-cli -regtest generatetoaddress 1 <your_regtest_address>
```

List transactions:
```bash
bitcoin-cli -regtest listtransactions
```

---



