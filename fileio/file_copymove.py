import shutil

#copy file
shutil.copy("hello.txt", "folder2")

#recursively copy an entire directory
shutil.copytree("folder2", "folder2_backup")

#move file
shutil.move("folder2/hello.txt", "folder2/anotherfolder")

#move and rename file
shutil.move("folder/anotherfolder/hello.txt", "folder2/anotherfolder/newhello.txt")
