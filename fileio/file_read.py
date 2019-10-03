#make sure you have a hello.txt in your current working directory
#same directory as your python script

helloFile = open("hello.txt")
content = helloFile.read()
print(content)
helloFile.close()


helloFile = open("hello.txt")
content = helloFile.readlines()
print(content)
helloFile.close()
