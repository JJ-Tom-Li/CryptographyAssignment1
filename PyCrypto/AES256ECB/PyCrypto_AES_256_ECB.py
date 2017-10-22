from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BlockSize = 16

def pad(raw):
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

class AES_ECB_Cipher:
    def __init__( self, key ):
        self.key = key
	self.iv = get_random_bytes(16)

    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_ECB, self.iv )
        return cipher.encrypt( raw )


    def decrypt( self, enc ):
        cipher = AES.new(self.key, AES.MODE_ECB, self.iv )
        return unpad(cipher.decrypt( enc ))

