from merkly.mtree import MerkleTree
from ecdsa import SigningKey, SECP256k1

# Step 1: Build Merkle Tree
data_blocks = ['block1', 'block2', 'block3', 'block4']
mtree = MerkleTree(data_blocks)
merkle_root = mtree.root
print("Merkle Root (hex):", merkle_root.hex())

# Step 2: Generate ECDSA Key Pair
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

# Step 3: Sign the Merkle Root
signature = sk.sign(merkle_root)
print("Signature (hex):", signature.hex())

# Step 4: Verify the Signature
is_valid = vk.verify(signature, merkle_root)
print("Signature valid?", is_valid)
