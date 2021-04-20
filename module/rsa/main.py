from Crypto.PublicKey import RSA

def generateKey():
    key = RSA.generate(1024)
    f = open('key/priv.pem', 'wb')
    f.write(key.exportKey())
    f.close()

    p = open('key/pub.pem', 'wb')
    p.write(key.publickey().exportKey())
    p.close()