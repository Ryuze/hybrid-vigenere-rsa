from Crypto.Hash import MD5

def hashMessage(message):
    md5Hash = MD5.new()
    md5Hash.update(message)
    
    return md5Hash.digest()