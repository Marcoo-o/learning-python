clear_text: str = "Krypto2026"
ct_b: bytes = clear_text.encode("utf-8")
key: int = 0x0F

def xor_cipher(data: bytes, key: int) -> bytes:
    return bytes(b^key for b in data)

enc = xor_cipher(ct_b, key)
print("Verschlüsselt (Hex):", enc.hex())

dec_bytes = xor_cipher(enc, key)
dec_text = dec_bytes.decode("utf-8")
print("Entschlüsselt:", dec_text)