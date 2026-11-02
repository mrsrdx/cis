import hashlib
from math import gcd

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
while gcd(e, phi) != 1:
    e += 1
d = mod_inverse(e, phi)

def hash_msg(msg):
    return int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n

message = "I agree to this contract"
h = hash_msg(message)
signature = pow(h, d, n)
verify_hash = pow(signature, e, n)
print("Message:", message)
print("Signature:", signature)
print("Valid signature:", verify_hash == h)

tampered_hash = hash_msg("I disagree with this contract")
print("Tampered message valid:", pow(signature, e, n) == tampered_hash)
