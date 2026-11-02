from math import gcd

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
while gcd(e, phi) != 1:
    e += 1
d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

msg = "HI"
encrypted = [pow(ord(ch), e, n) for ch in msg]
decrypted = "".join(chr(pow(c, d, n)) for c in encrypted)

print("Original:", msg)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
