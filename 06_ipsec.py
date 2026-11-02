import hmac
import hashlib

key = b"ipsec_key"
payload = b"Secret data packet"

def xor_encrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

encrypted = xor_encrypt(payload, key)
mac = hmac.new(key, encrypted, hashlib.sha256).hexdigest()

print("Original payload:", payload)
print("Encrypted (ESP-style):", encrypted)
print("Integrity Check (MAC):", mac)

decrypted = xor_encrypt(encrypted, key)
check_mac = hmac.new(key, encrypted, hashlib.sha256).hexdigest()

print("Decrypted:", decrypted)
print("Integrity OK:", check_mac == mac)
