#!/bin/sh
echo "Difference with AES256CBC:"
diff AES256CBC/$1_decryptedByAES256CBC.txt $1.txt
echo "Difference with AES256CTR:"
diff AES256CTR/$1_decryptedByAES256CTR.txt $1.txt
echo "Difference with AES256ECB:"
diff AES256ECB/$1_decryptedByAES256ECB.txt $1.txt
echo "Difference with RSA2048:"
diff RSA2048/$1_decryptedByRSA2048.txt $1.txt
echo "done"

