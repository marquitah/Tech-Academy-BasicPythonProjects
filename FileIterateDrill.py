#Your script will need to use Python 3 and the OS module.

import os

#Your script will need to use the listdir() method from
#the OS module to iterate through all files within a specific directory.

files = '/IterateFileDrill'

for files in os.listdir('/IterateFileDrill'):
    print(files)

#Your script will need to use the path.join() method from the OS module
#to concatenate the file name to its file path, forming an absolute path.

fName = '1.rtf'

fPath = '/IterateFileDrill'

gName = '2.rtf'

gPath = '/IterateFileDrill'

joinPath = os.path.join(fPath,fName)
print(joinPath)

joinPath2 = os.path.join(gPath,gName)
print(joinPath2)

#Your script will need to use the getmtime() method from the OS module
#to find the latest date that each text file has been created or modified.

pathTime1 = os.path.getmtime(joinPath)
pathTime2 = os.path.getmtime(joinPath2)

#Your script will need to print each file ending with a “.txt” file extension
#and its corresponding mtime to the console.

print(joinPath,pathTime1)
print(joinPath2,pathTime2)

