def block_xor(b1: bytes, b2: bytes) -> bytes:
    """Verknüpft zwei gleich lange Byte-Arrays per XOR"""
    return bytes(x ^ y for x, y in zip(b1, b2))

def dummy_block_cipher(block: bytes, key: bytes) -> bytes:
    """Simuliert eine 16-Byte Blockchiffre (Encrypt & Decrypt sind hier identisch)"""
    return block_xor(block, key)

def xex_encrypt(block: bytes, key: bytes, tweak: bytes) -> bytes:
    key1 = key[0:16]
    key2 = key[16:32]

    d = dummy_block_cipher(tweak, key2)
    ciphertext_blocks: list = []

    for i in range(0, len(block), 16):
        new_block = block[i:i+16]

        xor1 = block_xor(new_block, d)
        res = dummy_block_cipher(xor1, key1)
        ciphertext_block = block_xor(res, d)

        ciphertext_blocks.append(ciphertext_block)

        d = multiply_by_alpha(d)
    return b"".join(ciphertext_blocks)

def xex_decrypt(block: bytes, key: bytes, tweak: bytes) -> bytes:
    key1 = key[0:16]
    key2 = key[16:32]

    d = dummy_block_cipher(tweak, key2)
    plaintext_blocks: list = []
    
    for i in range(0, len(block), 16):
        new_block = block[i:i+16]

        xor1 = block_xor(new_block, d)
        res = dummy_block_cipher(xor1, key1)
        plaintext_block = block_xor(res, d)

        plaintext_blocks.append(plaintext_block)

        d = multiply_by_alpha(d)

    return b"".join(plaintext_blocks)

def multiply_by_alpha(tweak: bytes) -> bytes:
    """Multipliziert einen 16-Byte Tweak mit alpha im Galois-Körper"""
    # 1. Prüfen, ob das MSB (höchstwertigste Bit des ersten Bytes) 1 ist (Overflow)
    overflow = (tweak[0] & 0x80) != 0
    
    # 2. Alle Bytes als Integer in eine Liste umwandeln, damit wir damit rechnen können
    tweak_int = int.from_bytes(tweak, byteorder="big")
    
    # 3. Links-Shift um 1 Bit und auf 128 Bit (16 Bytes) begrenzen
    shifted = (tweak_int << 1) & ((1 << 128) - 1)
    
    if overflow:
        shifted ^= 0x87
        
    # 5. Wieder zurück in 16 Bytes (big-endian) konvertieren
    return shifted.to_bytes(16, byteorder="big")

key = b"1234567890123456ABCDEFGHIJKLMNOP"  # Exakt 32 Bytes!
tweak = b"SEKTOR_00000001"                  # Exakt 16 Bytes!
block = b"GeheimeDaten1234"                  # Exakt 16 Bytes!

# Verschlüsseln
ciphertext_block = xex_encrypt(block, key, tweak)
print("XEX Cipherblock (Hex):", ciphertext_block.hex())

# Entschlüsseln
plaintext_block = xex_decrypt(ciphertext_block, key, tweak)
print("Entschlüsselt:", plaintext_block.decode("utf-8"))