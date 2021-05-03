from module.rsa import main as rsa
from module.vigenere import main as vigenere
import time
import os.path
import sys

def generateRsaKey():
    if not checkRsaKeyExist():
        try:
            rsa.generateKey()
            return True
        except Exception as e:
            print(f'Failed: {e}')
            sys.exit()
        
def checkRsaKeyExist():
    if os.path.isfile('key/priv.pem') and os.path.isfile('key/pub.pem'):
        return True
    
def encrypt():
    start = time.perf_counter()
    generateRsaKey()
    initial_key = vigenere.generateUniqueKey()
    plaintext = "halo guys, david disini dan disini ada rice cooker pintar dari xiaomi. dia punya timer dan wifi didalamnya."
    ciphertext = vigenere.encrypt(plaintext, initial_key)
    key_enc = rsa.encrypt(initial_key)
    stop = time.perf_counter()
    
    print(f"Encrypt used time: {stop - start:0.4f} seconds")
    return ciphertext, key_enc

def decrypt(ciphertext, key):
    start = time.perf_counter()
    generateRsaKey()
    key_dec = rsa.decrypt(key)
    plaintext = vigenere.decrypt(ciphertext, key_dec)
    stop = time.perf_counter()
    
    print(f"Decrypt used time: {stop - start:0.4f} seconds")
    return plaintext

ciphertext, key = encrypt()
plaintext = decrypt(ciphertext, key)

print(f"""
ciphertext = {ciphertext}

key = {key}

plaintext = {plaintext}
      """)