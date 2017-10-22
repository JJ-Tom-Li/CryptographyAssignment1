import random
import os
def genSizeFile(fileName,fileSize):
	#filepath
	filePath = fileName+".txt"
	
	#datasize
	dataSize = 0
	with open(filePath,"w") as f:
		while dataSize < fileSize:
			f.write(str(random.choice('abcdefg&#%^*f')))
			f.write("\n")
			dataSize = os.path.getsize(filePath)

