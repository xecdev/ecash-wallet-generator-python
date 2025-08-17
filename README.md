# eCash Wallet Generator

A simple Python script to generate **eCash wallets** compatible with [Cashtab](https://cashtab.com), using the derivation path (`m/44'/1899'/0'/0/0`).

## Features
- Generates a 12-word mnemonic (BIP39).
- Generates a valid **eCash address** in `ecash:` format for the generated mnemonic.
- Derives private & public keys using BIP32 (Secp256k1).
- Fully compatible with Cashtab imports.

## ⚙️ Installation

## 📦 Install dependencies:
```
pip install -r requirements.txt
```
## 🛠 Usage
```
python app.py
```
## 📝 Output
Seed phrase: length want eyebrow stomach decide ocean spray gloom worth retreat quick panther

eCash address: ecash:qrqvhf0tqzjsqdt8xlc779fz7fuvppc8hcyct3kyjs
