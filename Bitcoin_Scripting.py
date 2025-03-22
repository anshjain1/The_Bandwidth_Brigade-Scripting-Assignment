from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_user = "your_username"
rpc_password = "your_password"
rpc_url = f"http://{rpc_user}:{rpc_password}@127.0.0.1:18443"
rpc_connection = AuthServiceProxy(rpc_url)

def create_wallet(wallet_name="mywallet"):
    """Creates and loads a Bitcoin wallet"""
    try:
        wallets = rpc_connection.listwallets()
        if wallet_name in wallets:
            print(f"✅ Wallet '{wallet_name}' is already loaded.")
            return

        rpc_connection.loadwallet(wallet_name)
        print(f"✅ Wallet '{wallet_name}' loaded.")

    except JSONRPCException:
        print(f"🔹 Wallet '{wallet_name}' does not exist. Creating...")
        rpc_connection.createwallet(wallet_name)
        print(f"✅ Wallet '{wallet_name}' created and loaded.")

def mine_blocks(num_blocks=101):
    """Mines blocks to generate test bitcoins"""
    miner_address = rpc_connection.getnewaddress()
    rpc_connection.generatetoaddress(num_blocks, miner_address)
    print(f"✅ Mined {num_blocks} blocks. Balance: {rpc_connection.getbalance()} BTC")

def generate_addresses(type="legacy"):
    """Generates three addresses for transactions"""
    addr_A = rpc_connection.getnewaddress("", type)
    addr_B = rpc_connection.getnewaddress("", type)
    addr_C = rpc_connection.getnewaddress("", type)
    print(f"🔹 {type} Address A: {addr_A}\n🔹 {type} Address B: {addr_B}\n🔹 {type} Address C: {addr_C}")
    return addr_A, addr_B, addr_C

def fund_address(address, amount=10):
    """Funds an address with test bitcoins"""
    txid = rpc_connection.sendtoaddress(address, amount)
    print(f"✅ Funded {address} with {amount} BTC. TXID: {txid}")
    rpc_connection.generatetoaddress(1, rpc_connection.getnewaddress()) 
    return txid

def create_transaction(from_addr, to_addr, amount):
    """Creates, signs, and broadcasts a transaction"""
    utxos = rpc_connection.listunspent(1, 9999999, [from_addr])
    if not utxos:
        print(f"❌ No UTXOs available for {from_addr}")
        return None

    utxo = utxos[0]
    txid = utxo["txid"]
    vout = utxo["vout"]
    balance = float(utxo["amount"]) 
    fee = 0.0001
    change = balance - amount - fee

    inputs = [{"txid": txid, "vout": vout}]
    outputs = {to_addr: amount, from_addr: change}

    raw_tx = rpc_connection.createrawtransaction(inputs, outputs)
    signed_tx = rpc_connection.signrawtransactionwithwallet(raw_tx)
    txid = rpc_connection.sendrawtransaction(signed_tx["hex"])

    print(f"✅ Transaction {from_addr} → {to_addr} Sent! TXID: {txid}")
    rpc_connection.generatetoaddress(1, rpc_connection.getnewaddress()) 
    return txid

def decode_transaction(txid):
    """Decodes a transaction and prints script details"""
    raw_tx = rpc_connection.getrawtransaction(txid, True)
    print(f"🔎 Decoded Transaction {txid}:")
    print(raw_tx)
    return raw_tx

def extract_challenge_script(txid):
    raw_tx = rpc_connection.getrawtransaction(txid, True)
    print(f"  - Locking Script (ScriptPubKey): {raw_tx['vout'][0]['scriptPubKey']['asm']}")

def extract_response_script(txid):
    raw_tx = rpc_connection.getrawtransaction(txid, True)
    print(f"  - Unlocking Script (ScriptSig): {raw_tx['vin'][0]['scriptSig']['asm'] if 'scriptSig' in raw_tx['vin'][0] else 'N/A'}")

def compare_transaction_sizes(txid1, txid2):
    """Compares transaction sizes of Legacy and SegWit transactions"""
    size1 = rpc_connection.getrawtransaction(txid1, True)["vsize"]
    size2 = rpc_connection.getrawtransaction(txid2, True)["vsize"]
    print(f"📊 Legacy Transaction Size: {size1} vbytes")
    print(f"📊 SegWit Transaction Size: {size2} vbytes")

# 🚀 Main Execution 🚀
if __name__ == "__main__":
    print("🔹 Setting up Bitcoin Environment...")
    create_wallet()
    mine_blocks()

    print("\n🔹 Generating Legacy (P2PKH) Addresses...")
    addr_A, addr_B, addr_C = generate_addresses("legacy")

    print("\n🔹 Funding Address A...")
    fund_txid = fund_address(addr_A)

    print("\n🔹 Creating Transaction (A → B)...")
    txid_AB = create_transaction(addr_A, addr_B, 2)

    print("\n🔹 Decoding Legacy Transaction (A → B)...")
    decode_transaction(txid_AB)

    print("\n🔹 Extracting Challenge Script (A → B)...")
    extract_challenge_script(txid_AB)

    print("\n🔹 Creating Transaction (B → C)...")
    txid_BC = create_transaction(addr_B, addr_C, 1)

    print("\n🔹 Decoding Legacy Transaction (B → C)...")
    decode_transaction(txid_BC)

    print("\n🔹 Extracting Response Script (B → C)...")
    extract_response_script(txid_BC)

    print("\n🔹 Generating SegWit (P2SH-P2WPKH) Addresses...")
    addr_A_segwit, addr_B_segwit, addr_C_segwit = generate_addresses("p2sh-segwit")

    print("\n🔹 Funding SegWit Address A'...")
    fund_txid_segwit = fund_address(addr_A_segwit)

    print("\n🔹 Creating Transaction (A' → B')...")
    txid_AB_segwit = create_transaction(addr_A_segwit, addr_B_segwit, 2)

    print("\n🔹 Decoding SegWit Transaction (A' → B')...")
    decode_transaction(txid_AB_segwit)

    print("\n🔹 Extracting Challenge Script (A' → B')...")
    extract_challenge_script(txid_AB_segwit)

    print("\n🔹 Creating Transaction (B' → C')...")
    txid_BC_segwit = create_transaction(addr_B_segwit, addr_C_segwit, 1)

    print("\n🔹 Decoding SegWit Transaction (B' → C')...")
    decode_transaction(txid_BC_segwit)

    print("\n🔹 Extracting Response Script (B' → C')...")
    extract_response_script(txid_BC_segwit)

    print("\n🔹 Comparing Transaction Sizes...")
    
    print("\n✅  (A → B) and (A' → B')-")
    compare_transaction_sizes(txid_AB, txid_AB_segwit)

    print("\n✅  (B → C) and (B' → C')-")
    compare_transaction_sizes(txid_BC, txid_BC_segwit)

    print("\n✅ Bitcoin Scripting Assignment Completed!")
