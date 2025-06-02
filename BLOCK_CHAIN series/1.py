import hashlib
import random
import time

# -------------------- Simulation Parameters -------------------- #
# Transactions from IoT devices
transactions = [
    "SmartMeter_1: User_A used 1.2 kWh at 3:00 PM",
    "TrafficSensor_5: Detected congestion at Junction 7",
    "SmartLock_3: Door opened at 2:45 PM by User_B"
]

# Mining gateways for PoW
pow_gateways = ["Gateway_A", "Gateway_B", "Gateway_C"]
difficulty = 4  # number of leading zeros required in hash

# Staking for PoS
pos_stakes = {
    "Gateway_A": 10,
    "Gateway_B": 50,
    "Gateway_C": 5
}

# -------------------- Proof of Work Simulation -------------------- #
def proof_of_work(block_data, difficulty):
    nonce = 0
    while True:
        block = f"{block_data}|{nonce}"
        block_hash = hashlib.sha256(block.encode()).hexdigest()
        if block_hash.startswith('0' * difficulty):
            return nonce, block_hash
        nonce += 1

# Simulate PoW
pow_start = time.time()
pow_winner = random.choice(pow_gateways)  # Simulated miner who finds the block first
block_data_pow = '|'.join(transactions)
nonce, pow_hash = proof_of_work(block_data_pow, difficulty)
pow_time = time.time() - pow_start

# -------------------- Proof of Stake Simulation -------------------- #
def choose_pos_validator(stakes):
    total_stake = sum(stakes.values())
    rand = random.uniform(0, total_stake)
    cumulative = 0
    for gateway, stake in stakes.items():
        cumulative += stake
        if rand <= cumulative:
            return gateway

# Simulate PoS
pos_start = time.time()
pos_validator = choose_pos_validator(pos_stakes)
block_data_pos = '|'.join(transactions)
block_hash_pos = hashlib.sha256(block_data_pos.encode()).hexdigest()
pos_time = time.time() - pos_start

# -------------------- Output -------------------- #
print("\n--- Proof of Work ---")
print(f"Winner: {pow_winner}")
print(f"Nonce: {nonce}")
print(f"Hash: {pow_hash}")
print(f"Time Taken (seconds): {round(pow_time, 4)}")

print("\n--- Proof of Stake ---")
print(f"Validator: {pos_validator}")
print(f"Hash: {block_hash_pos}")
print(f"Time Taken (seconds): {round(pos_time, 4)}")
