from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BlockSize = 16
#pad = lambda s: s + (BlockSize - len(s) % BlockSize) * chr(BlockSize - len(s) % BlockSize)
#unpad = lambda s : s[:-ord(s[len(s)-1:])]

def pad(raw):
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

count = get_random_bytes(16)
class AES_CTR_Cipher:
    def __init__( self, key ):
        self.key = key
	count = get_random_bytes(16)
	
    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CTR, counter = lambda:count )
        return cipher.encrypt( raw )


    def decrypt( self, enc ):
        cipher = AES.new(self.key, AES.MODE_CTR,counter = lambda:count)
        return unpad(cipher.decrypt( enc ))

