"""
A Caesar cipher is one of the simplest and oldest forms of encryption, named after Julius Caesar, who reportedly used it to send secret messages to his generals.
The Caesar cipher works by performing a shift on the letters of the input text using a fixed key (a number between 0 and 25). 
Each letter in the original message is shifted forward or backward by the key value to obtain the encrypted message (ciphertext).

For example, with a key of 3:

A → D
B → E
C → F
This pattern continues, with the shift wrapping around to the beginning of the alphabet if necessary (for example, Z shifted by 3 becomes C).

Requirements:
1. Write a function caesar_encrypt(text, key) that performs the encryption.
2. Write a function caesar_decrypt(text, key) that performs the decryption.
3. Test the solution with different keys and edge cases.
"""

# 1. encipher
def caesar_encrypt(text, key):
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
    I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    ciphertext = ""
    for c in text:
        if c.isalpha():
            shifted = (L2I[c.upper()] + key) % 26
            encrypted_char = I2L[shifted]
            ciphertext += encrypted_char if c.isupper() else encrypted_char.lower()
        else:
            ciphertext += c
    return ciphertext

# 2. decipher
def caesar_decrypt(text, key):
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
    I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    plaintext = ""
    for c in text:
        if c.isalpha():
            shifted = (L2I[c.upper()] - key) % 26
            decrypted_char = I2L[shifted]
            plaintext += decrypted_char if c.isupper() else decrypted_char.lower()
        else:
            plaintext += c
    return plaintext


L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key = 7
plaintext = "DEFEND THE EAST WALL OF THE CASTLE"

print(plaintext)
print(caesar_encrypt(plaintext))
print(caeser_decrypt(plaintext))
