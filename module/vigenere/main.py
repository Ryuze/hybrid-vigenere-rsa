import random
import secrets
from ordered_set import OrderedSet

def __originalTable():
    table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    
    return table
    
def scrambleTable(key):
    table = __originalTable()
    
    random.Random(key).shuffle(table)
    
    return table

def generateUniqueKey():
    unique_key = secrets.token_urlsafe()
    
    return unique_key

def stretchKey(table, initialKey, plaintextLength):    
    random.seed(initialKey)
    key = random.choices(table, k=plaintextLength)
    
    return key

def encrypt(plaintext, initial_key):
    table = scrambleTable(initial_key)
    key = stretchKey(table, initial_key, len(plaintext))
    cipher = []
    
    for index in range(len(plaintext)):
        calculate = (table.index(plaintext[index]) + table.index(key[index])) % 95
        cipher.append(table[calculate])
    
    return ''.join(cipher)

def decrypt(ciphertext, initial_key):
    table = scrambleTable(initial_key)
    key = stretchKey(table, initial_key, len(ciphertext))
    plain = []

    for index in range(len(ciphertext)):
        calculate = (table.index(ciphertext[index]) - table.index(key[index])) % 95
        plain.append(table[calculate])
    
    return ''.join(plain)

if __name__ == "__main__":
    plaintext = "In cryptography, encryption is the process of encoding information. This process converts the original representation of the information, known as plaintext, into an alternative form known as ciphertext. Ideally, only authorized parties can decipher a ciphertext back to plaintext and access the original information."
    token = 'sxOrtLSsHauQcF7pQMNYalIDCC27Uparg_4QLUv6j9w'
    tabel = scrambleTable(token)
    primaryKey = ''.join(stretchKey(tabel, token, len(plaintext)))
    # secondaryKey = ''.join(fakeStretchKey(token, len(plaintext)))
    enc = encrypt(plaintext, token)
    
    print(f'Token yang digunakan: {token}')
    print()
    print(f"""Hasil enkripsi:
{enc}""")
    print()
#     print(f"""Key dengan tabel tidak diacak:
# {secondaryKey}""")
    # print(f'Tabel: {tabel}')