from genFile.genFile import genSizeFile
from RSA2048.PyCrypto_RSA_2048 import *
from AES256CBC.PyCrypto_AES_256_CBC import AES_CBC_Cipher
from AES256ECB.PyCrypto_AES_256_ECB import AES_ECB_Cipher
from AES256CTR.PyCrypto_AES_256_CTR import AES_CTR_Cipher
from RSA2048.PyCrypto_RSA_2048 import RSA_2048_Cipher
from SHA512.PyCrypto_SHA_512 import SHA_512_Cipher
from Crypto.Random import get_random_bytes
import os
import sys
import time

#generate a file
filename = "16MB+7byte"
genSizeFile(filename,16*1000*1000+7)
print("File generate done.")

#encrypt and decrypt with AES 256 CBC
with open("AES256CBC/"+filename+"_encryptedByAES256CBC.txt","wb") as f1:
	#open the plaintext
	data = open(filename+".txt").read()
	
	#generate key
	key=get_random_bytes(16)
	
	#generate IV
	IV = get_random_bytes(16)
	
	print("AES-256-CBC encryption start:")
	start = time.time()
	
	#encrypt
	ciphertext = AES_CBC_Cipher(key,IV).encrypt(data)
	
	end = time.time()	
	print("AES-256-CBC encryption end.")
	print("AES-256-CBC encryption spend "+str(round((end-start),5))+" seconds.")

	#output to file
	f1.write(ciphertext)

	print("AES-256-CBC decryption start:")
	start = time.time()

	#decrypt
	plaintext = AES_CBC_Cipher(key,IV).decrypt(ciphertext)
	
	end = time.time()	
	print("AES-256-CBC decryption end.")
	print("AES-256-CBC decryption spend "+str(round((end-start),5))+" seconds.")
	
	with open("AES256CBC/"+filename+"_decryptedByAES256CBC.txt","w") as fout1:
		fout1.write(plaintext)
print("AES256CBC done.")

#encrypt and decrypt with AES 256 ECB
with open("AES256ECB/"+filename+"_encryptedByAES256ECB.txt","wb") as f2:
	
	#generate key
	key=get_random_bytes(16)

	print("AES-256-ECB encryption start:")
	start = time.time()

	#encrypt
	ciphertext = AES_ECB_Cipher(key).encrypt(data)
	
	end = time.time()	
	print("AES-256-ECB encryption end.")
	print("AES-256-ECB encryption spend "+str(round((end-start),5))+" seconds.")
	
	#output to file
	f2.write(ciphertext)

	print("AES-256-ECB decryption start:")
	start = time.time()

	#decrypt
	plaintext = AES_ECB_Cipher(key).decrypt(ciphertext)

	end = time.time()	
	print("AES-256-ECB decryption end.")
	print("AES-256-ECB decryption spend "+str(round((end-start),5))+" seconds.")

	with open("AES256ECB/"+filename+"_decryptedByAES256ECB.txt","wb") as fout2:
		fout2.write(plaintext)
print("AES256ECB done.")

#encrypt and decrypt with AES 256 CTR
with open("AES256CTR/"+filename+"_encryptedByAES256CTR.txt","wb") as f3:
	
	#generate key
	key=get_random_bytes(16)

	print("AES-256-CTR encryption start:")
	start = time.time()

	#encrypt
	ciphertext = AES_CTR_Cipher(key).encrypt(data)

	end = time.time()	
	print("AES-256-CTR encryption end.")
	print("AES-256-CTR encryption spend "+str(round((end-start),5))+" seconds.")

	#output to file
	f3.write(ciphertext)

	print("AES-256-CTR decryption start:")
	start = time.time()

	#decrypt
	plaintext = AES_CTR_Cipher(key).decrypt(ciphertext)

	end = time.time()	
	print("AES-256-CTR decryption end.")
	print("AES-256-CTR decryption spend "+str(round((end-start),5))+" seconds.")

	with open("AES256CTR/"+filename+"_decryptedByAES256CTR.txt","w") as fout3:
		fout3.write(plaintext)
print("AES256CTR done.")

#encrypt and decrypt with RSA 2048
with open("RSA2048/"+filename+"_encryptedByRSA2048.txt","wb") as f4:
	
	#generate public and private keys
	RSA_2048_Cipher().CreateRSAKeys("123456")

	print("RSA-2048 encryption start:")
	start = time.time()

	#encrypt
	ciphertext = RSA_2048_Cipher().encrypt(data)

	end = time.time()	
	print("RSA-2048 encryption end.")
	print("RSA-2048 encryption spend "+str(round((end-start),5))+" seconds.")

	#output to file
	f4.write(ciphertext)

	print("RSA-2048 decryption start:")
	start = time.time()

	#decrypt
	plaintext = RSA_2048_Cipher().decrypt(ciphertext,"123456")

end = time.time()	
print("RSA-2048 decryption end.")
print("RSA-2048 decryption spend "+str(round((end-start),5))+" seconds.")

with open("RSA2048/"+filename+"_decryptedByRSA2048.txt","w") as fout4:
	fout4.write(plaintext)
print("RS2048 done.")

#hash with SHA 512
with open("SHA512/"+filename+"_encryptedBySHA512.txt","wb") as f5:
	
	print("SHA-512 encryption start:")
	start = time.time()

	#hash
	ciphertext = SHA_512_Cipher().hash(data)
	
	end = time.time()	
	print("SHA-512 encryption end.")
	print("SHA-512 encryption spend "+str(round((end-start),5))+" seconds.")

	f5.write(ciphertext)
print("SHA512 done.")
