cipher_hex = "0d447d767f7b603d3f3d39"

cipher_bytes = bytes.fromhex(cipher_hex)

def xor_cipher(data: bytes, key: int) -> bytes:
    return bytes(b^key for b in data)

for key in range(256):
    clear_bytes = xor_cipher(cipher_bytes, key)
    clear_text = clear_bytes.decode("utf-8", errors="ignore")

    if clear_text.isprintable():
        print(f"Key: {hex(key)} ({key:3d}):", clear_text)