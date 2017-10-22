from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization,hashes

def pad(raw,BlockSize):
	#Padding the data by BlockSize
	padnumber = (BlockSize - len(raw) % BlockSize)
	return raw + padnumber * chr(padnumber)

def unpad(raw):
	unpadnumber = raw[len(raw)-1]
	return raw[:-ord(unpadnumber)]

class RSA_2048_Cipher:
	def __init__(self):
		pass
	def CreateRSAKeys(self,code):
		#generate RSA private key
		private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
		
		#Transform key into bytes
		pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,
		encryption_algorithm=serialization.BestAvailableEncryption(code))
		
		#Put the key into file
		pem.splitlines()[0]
		with open("RSA2048/private_rsa_key.bin","wb") as f:
			f.write(pem)
	
		#generate public key
		public_key = private_key.public_key()

		#Transform key into bytes
		pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

		#Put the key into file
		pem.splitlines()[0]
		with open("RSA2048/public_rsa_key.pem","wb") as f:
			f.write(pem)

	def encrypt(self,data):
		
		#import public key 
		public_key = serialization.load_pem_public_key(open("RSA2048/public_rsa_key.pem").read(),backend=default_backend())
		
		#Get the buffer size
		buffer_size = 214

		ciphertext=[]

		#Get the length of input data
		data_size = len(data)
		
		j = 1
		#Encrypt the data 
		for i in range(0, data_size, buffer_size):
			if(float(i*100)/data_size>=j):
				#Show the progress rate
				print("Has finished "+str(j)+"%.")
				j+=1
			#Encrypt the data with public key	
			ciphertext.append(public_key.encrypt(data[i:i+buffer_size],padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label=None)))
		
		return "".join(ciphertext)

	def decrypt(self,data,code):
		#import private key with code
		private_key = serialization.load_pem_private_key(
open("RSA2048/private_rsa_key.bin").read(),password=code, backend=default_backend())
		
		#Get the buffer size
		buffer_size = 256

		#Get the length of input data
		data_size = len(data)
		
		plaintext = []

		j = 1
		#Encrypt the data 
		for i in range(0, data_size, buffer_size):
			if(float(i*100)/data_size>=j):
				#Show the progress rate
				print("Has finished "+str(j)+"%.")
				j+=1	
			#Decrypt the data with public key
			plaintext.append(private_key.decrypt(data[i:i+buffer_size],padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label=None)))
		
		return "".join(plaintext)
