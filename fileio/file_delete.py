import os

print(os.getcwd())

#delete directory
os.rmdir("folder2_backup")

import shutil
#delete directory
shutil.rmtree("folder2_backup")


import send2trash
send2trash.send2trash("D:\\etc etc")

