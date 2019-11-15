import shutil
import os


#copy file  src         target
if os.path.isdir("folder2") == False:
    os.makedirs("folder2")
if os.path.isfile("folder2/hello.txt") == False:
    shutil.copy("hello.txt", "folder2")
else:
    os.remove("folder2/hello.txt")
    shutil.copy("hello.txt", "folder2")

#recursively copy an entire directory
if os.path.isdir("folder2_backup") == False:
    shutil.copytree("folder2", "folder2_backup")

#move file

if os.path.isdir("folder2/anotherfolder") == False:
    os.makedirs("folder2/anotherfolder")
else:
    shutil.move("folder2/hello.txt", "folder2/anotherfolder")

#move and rename file
shutil.move("folder2/anotherfolder/hello.txt", "folder2/anotherfolder/newhello.txt")
