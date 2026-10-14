clear: str = "Kryptoanalyse macht Spass!"
clear_b = clear.encode("utf-8")

key = b"KEY"

def repeating_key_xor(data: bytes, key: bytes) -> bytes:
    cipher: list = []
    for i, byte in enumerate(data):
        key_byte = key[i % len(key)]
        cipher.append(byte^key_byte)
    return bytes(cipher)

cipher_b: bytes = repeating_key_xor(clear_b, key)
clear_new_b: bytes = repeating_key_xor(cipher_b, key)

print(f"Verschlüsselt: {clear} -> {cipher_b.hex()}")
print(f"Entschlüsselt: {cipher_b} -> {clear_new_b.decode("utf-8")}")
