from Crypto.PublicKey import RSA


# Generate (First time)
# f_priv = open('keys/priv','w')
#
# f_pub = open('keys/pub','w')
#
# private = RSA.generate(2048)
# public  = private.publickey()
# f_priv.write(private.exportKey())
# f_pub.write(public.exportKey())
def decrypt(msg):
    with open('keys/priv', 'r') as content_file:
        f_priv = content_file.read()
    keyPriv = RSA.importKey(f_priv)
    return keyPriv.decrypt(msg)
