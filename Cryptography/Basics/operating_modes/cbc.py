def block_xor(b1: bytes, b2: bytes) -> bytes:
    """Verknüpft zwei gleich lange Byte-Arrays per XOR"""
    return bytes(x ^ y for x, y in zip(b1, b2))

def dummy_block_cipher(block: bytes, key: bytes) -> bytes:
    """Simuliert eine 16-Byte Blockchiffre (Encrypt & Decrypt sind identisch)"""
    return block_xor(block, key)

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

def cbc_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    paded_data = pad_pkcs7(data, 16)

    previous_cipher = iv
    ciphertext_blocks = []
    for i in range(0, len(paded_data), 16):
        block = paded_data[i:i+16]
        res = block_xor(block, previous_cipher)
        current_cipher = dummy_block_cipher(res, key)        
        ciphertext_blocks.append(current_cipher)
        previous_cipher = current_cipher
    return b"".join(ciphertext_blocks)

def cbc_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    previous_cipher = iv
    plaintext_blocks = []

    for i in range(0, len(data), 16):
        block = data[i:i+16]
        decrypted_block = dummy_block_cipher(block, key)
        res = block_xor(decrypted_block, previous_cipher)
        plaintext_blocks.append(res)
        previous_cipher = block
    raw_plain = b"".join(plaintext_blocks)
    return unpad_pkcs7(raw_plain)
    

key = b"1234567890123456"  # 16 Bytes Key
iv  = b"INIT_VECTOR_1234"  # 16 Bytes IV
secret_msg = b"Angriff auf CBC!"

# Verschlüsseln
ciphertext = cbc_encrypt(secret_msg, key, iv)
print("Ciphertext (Hex):", ciphertext.hex())

# Entschlüsseln
plaintext = cbc_decrypt(ciphertext, key, iv)
print("Entschlüsselt:", plaintext.decode("utf-8"))