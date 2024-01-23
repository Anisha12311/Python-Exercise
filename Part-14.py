import os
import shutil
path = 'test.txt'

if os.path.exists(path):
    print("Path is correct")
    if os.path.isfile(path):
        print("This is file")
    elif os.path.isdir(path):
        print("THis is directory")
else :
    print("Path is worng")
    
    
    
with open(path) as file:
    print(file.read())
    
print(file.closed)
text = "New lines \n yeah there!"
with open(path, 'w') as file :
    file.write(text)
    
    
shutil.copyfile("test.txt","copyfile.txt")
# shutil.copy("test.txt","copy.txt")  # copy permission mode and destination can be directory
shutil.copy2("test.txt", "copy2.txt")

os.remove('copy.txt')
os.rmdir('folder')
shutil.rmtree('foldercontians file')