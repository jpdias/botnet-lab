from Crypto.PublicKey import RSA
import base64

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
    keypriv = RSA.importKey(f_priv)
    msg = base64.b64decode(msg)
    return keypriv.decrypt(msg)
