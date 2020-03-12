import os
import shutil

for folderName, subfolders, filenames in os.walk('target'):
    for filename in filenames:
        print('Checking file: ' + filename + " in folder: " + folderName)

        #content reading
        fin = open(folderName+"/"+filename)
        content = fin.read()
        fin.close()

        #content processing
        if content.find("Hello World") != -1:
            print("FOUND at " + folderName+"/"+filename)
            shutil.move(folderName+"/"+filename, folderName+"/" + "goal.txt")


