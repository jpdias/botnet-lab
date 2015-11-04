from Crypto.PublicKey import RSA
import urllib2


def encrypt(msg):
    # with open('keys/pub', 'r') as content_file:
    #    f_pub = content_file.read()
    url_public_key = urllib2.urlopen('http://pastebin.com/raw.php?i=UcxTLbqY').read();
    keyPub = RSA.importKey(url_public_key)
    crypto_msg = keyPub.encrypt(msg, 32)
    return crypto_msg;
