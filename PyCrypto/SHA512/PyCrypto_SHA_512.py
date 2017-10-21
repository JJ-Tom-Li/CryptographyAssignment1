from Crypto.Hash import SHA512


class SHA_512_Cipher:
	
	def __init__( self):
		pass

	def hash(self,data):
		h = SHA512.new()
		h.update(data)
		return h.hexdigest()
