P = 23
G = 5

a_private = 6
a_public = pow(G, a_private, P)

b_private = 15
b_public = pow(G, b_private, P)

alice_secret = pow(b_public, a_private, P)
bob_secret = pow(a_public, b_private, P)

print("Alice public key:", a_public)
print("Bob public key:", b_public)
print("Alice's shared secret:", alice_secret)
print("Bob's shared secret:", bob_secret)
print("Match:", alice_secret == bob_secret)
