from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def pad(raw,BlockSize):
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

class RSA_2048_Cipher:
	def __init__(self):
		pass
	def CreateRSAKeys(self,code):
		#generate RSA 2048 bit key
		key = RSA.generate(2048)
		encrypted_key = key.exportKey(passphrase=code,pkcs=8)
	
		#generate private key
		with open("RSA2048/private_rsa_key.bin","wb") as f:
			f.write(encrypted_key)
	
		#generate public key
		with open("RSA2048/public_rsa_key.pem","wb") as f:
			f.write(key.publickey().exportKey())

	def encrypt(self,data):
		
		#import public key 
		public_key = RSA.importKey(open('RSA2048/public_rsa_key.pem').read())
		
		#Get the buffer size
		buffer_size = 214
	
		#Padding the public key
		cipher_rsa = PKCS1_OAEP.new(public_key)
		ciphertext=[]
		
		#Get the length of input data
		data_size = len(data)
		
		j = 1
		#Encrypt the data 
		for i in range(0, data_size, buffer_size):
			if(float(i*100)/data_size>=j):
				print("Has finished "+str(j)+"%.")
				j+=1	
			ciphertext.append(cipher_rsa.encrypt(data[i:i+buffer_size]))
		
		return "".join(ciphertext)

	def decrypt(self,data,code):
		#import private key
		private_key = RSA.importKey(open("RSA2048/private_rsa_key.bin").read(),passphrase=code)
		
		#Get the buffer size
		buffer_size = 256

		#Get the length of input data
		data_size = len(data)

		#Padding the private key
		cipher_rsa = PKCS1_OAEP.new(private_key)
		
		plaintext = []

		j = 1
		#Encrypt the data 
		for i in range(0, data_size, buffer_size):
			if(float(i*100)/data_size>=j):
				print("Has finished "+str(j)+"%.")
				j+=1	
			plaintext.append(cipher_rsa.decrypt(data[i:i+buffer_size]))
		return "".join(plaintext)
