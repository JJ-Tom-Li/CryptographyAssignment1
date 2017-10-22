#Hash the data with SHA-512
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class SHA_512_Cipher:
	
	def __init__( self):
		pass

	def hash(self,data):
		digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
		digest.update(data)
		return digest.finalize()
