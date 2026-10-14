def pad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len

def unpad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
    pad_len = data[-1]
    
    if pad_len < 1 or pad_len > block_size or pad_len > len(data):
        raise ValueError("Invalid Padding")

    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid Padding2")

    return data[:-pad_len]

# Test 1: 6 Bytes Lang (Blocksize 16) -> erwartet 10 Bytes Padding (Wert 10)
data1 = b"Krypto"
padded1 = pad_pkcs7(data1)
print("Padded 1 (Hex):", padded1.hex())
print("Unpadded 1:", unpad_pkcs7(padded1))

# Test 2: Genau 16 Bytes Lang -> erwartet 16 zusätzliche Bytes (Wert 16)
data2 = b"YELLOW SUBMARINE"
padded2 = pad_pkcs7(data2)
print("Padded 2 Länge:", len(padded2))  # Sollte 32 sein!