#!/bin/sh
rm -f $1.txt 
rm -f AES256CBC/$1_decryptedByAES256CBC.txt
rm -f AES256CBC/$1_encryptedByAES256CBC.txt

rm -f AES256CTR/$1_decryptedByAES256CTR.txt
rm -f AES256CTR/$1_encryptedByAES256CTR.txt

rm -f AES256ECB/$1_decryptedByAES256ECB.txt 
rm -f AES256ECB/$1_encryptedByAES256ECB.txt 

rm -f RSA2048/$1_decryptedByRSA2048.txt
rm -f RSA2048/$1_encryptedByRSA2048.txt

rm -f SHA512/$1_encryptedBySHA512.txt
rm -f RSA2048/private_rsa_key.bin
rm -f RSA2048/public_rsa_key.pem

