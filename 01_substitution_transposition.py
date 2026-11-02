def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def transposition_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    order = sorted(range(cols), key=lambda i: key[i])
    rows = [text[i:i+cols] for i in range(0, len(text), cols)]
    result = ""
    for col in order:
        for row in rows:
            if col < len(row):
                result += row[col]
    return result

msg = "ATTACK AT DAWN"
print("Original:", msg)

enc = caesar_encrypt(msg, 3)
print("Caesar Encrypted:", enc)
print("Caesar Decrypted:", caesar_decrypt(enc, 3))

enc2 = transposition_encrypt(msg, "KEY")
print("Transposition Encrypted:", enc2)
