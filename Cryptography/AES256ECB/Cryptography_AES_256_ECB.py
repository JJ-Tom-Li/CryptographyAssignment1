#Encrypt data with AES 256 ECB
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

#Size of the block for encryption
BlockSize = 16

def pad(raw):
	#Padding the data with PKCS
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

class AES_ECB_Cipher:
    def __init__( self, key ):
	#initialize
        self.key = key
	self.backend = default_backend()
	
    def encrypt( self, raw ):
	#padding the raw
	raw = pad(raw)

	#Initialize cipher
	cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=self.backend)
	
	#Create encryptor
	encryptor = cipher.encryptor()

	#Encrypt the data
	raw = encryptor.update(raw)
	return raw


    def decrypt( self, enc ):
	#Initialize cipher
	cipher = Cipher(algorithms.AES(self.key), modes.ECB(), backend=self.backend)

	#Create decryptor
	decryptor = cipher.decryptor()
	
	#Decrypt and unpad data
        return unpad(decryptor.update(enc))
