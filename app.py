from bip_utils import (
    Bip39MnemonicGenerator, Bip39SeedGenerator,
    Bip32Slip10Secp256k1, P2PKHAddr
)
from ecashaddress.convert import Address

# 1. Generate 12-word mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)
print("Seed phrase:", mnemonic)

# 2. Convert mnemonic into seed bytes
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# 3. Initialize BIP32 master node (secp256k1 curve)
bip32_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)

# 4. Derive eCash path: m/44'/1899'/0'/0/0 (compatible with Cashtab.com wallet)
path = "m/44'/1899'/0'/0/0"
child_key = bip32_ctx.DerivePath(path)

# 5. Extract raw Secp256k1 pubkey object from Bip32PublicKey
pub_key_obj = child_key.PublicKey().KeyObject()   # <-- This gives Secp256k1PublicKey

# 6. Encode legacy base58 P2PKH address (Bitcoin-style) with net_ver=0x00
legacy_addr = P2PKHAddr.EncodeKey(pub_key_obj, net_ver=b"\x00")

# 7. Convert legacy → ecash cashaddr using ecashaddress lib
ecash_addr = Address.from_string(legacy_addr).to_cash_address(prefix="ecash")

print("eCash address:", ecash_addr)
