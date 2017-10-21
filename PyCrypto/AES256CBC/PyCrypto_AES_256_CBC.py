from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
BlockSize = 16

#padding 
#pad = lambda s: s + (BlockSize - len(s) % BlockSize) * chr(BlockSize - len(s) % BlockSize)
#unpadding
#unpad = lambda s : s[:-ord(s[len(s)-1:])]

def pad(raw):
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

class AES_CBC_Cipher:
    def __init__( self, key,IV):
	#initialize
		self.key = key
		self.iv = IV
    def encrypt( self, raw ):
	#padding the raw
        raw=pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return cipher.encrypt( raw )


    def decrypt( self, enc ):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return unpad(cipher.decrypt( enc ))
	
	
