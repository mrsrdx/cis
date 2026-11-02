import hmac
import hashlib

key = b"secretkey"
message = b"Transfer $500"

mac = hmac.new(key, message, hashlib.sha256).hexdigest()
print("Message:", message.decode())
print("MAC:", mac)

check1 = hmac.new(key, message, hashlib.sha256).hexdigest()
print("Valid message check:", check1 == mac)

tampered = b"Transfer $9000"
check2 = hmac.new(key, tampered, hashlib.sha256).hexdigest()
print("Tampered message check:", check2 == mac)
