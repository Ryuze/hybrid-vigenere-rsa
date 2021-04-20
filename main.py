from module.rsa import main as rsa
from module.vigenere import main as vigenere
import os.path

def rsaKey():
    if checkFileExist():
        print('ada file nya')
    else:
        print('file tidak ada, membuat sekarang')
        rsa.generateKey()
        print('file berhasil dibuat')
        
def checkFileExist():
    if os.path.isfile('key/priv.pem') and os.path.isfile('key/pub.pem'):
        return True

def vigenereKey(key):
    a = vigenere.scrambleTable(key)
    return a
    
print(vigenereKey('idiotka'))