import os
where = "D:\\PythonWorkshop"

def listFiles(where):
    for folderName, subfolders, filenames in os.walk(where):
        for file in filenames:
            print(os.path.join(folderName,file))

listFiles(where)

def totalFileSize(where):
    totalSize = 0
    for folderName, subfolders, filenames in os.walk(where):
        for file in filenames:
            totalSize += os.path.getsize(os.path.join(folderName, file))
    return totalSize

print("Total is %d"%totalFileSize(where))


