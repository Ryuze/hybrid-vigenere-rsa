from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generateKey():
    key = RSA.generate(1024)
    f = open('key/priv.pem', 'wb')
    f.write(key.exportKey())
    f.close()

    p = open('key/pub.pem', 'wb')
    p.write(key.publickey().exportKey())
    p.close()
    
def encrypt(plaintext):
    message = plaintext.encode('utf-8')
    key = RSA.importKey(open('key/pub.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    
    return ciphertext

def decrypt(ciphertext):
    key = RSA.importKey(open('key/priv.pem').read())
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext).decode()
    
    return plaintext