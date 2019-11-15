#make sure you have a hello.txt in your current working directory
#same directory as your python script

# helloFile = open("hello.txt")
# content = helloFile.read()
# print(content)
# helloFile.close()


helloFile = open("hello.txt")
content = helloFile.readlines()
print(content)
helloFile.close()

for i in range(len(content)):
    print (content[i])
    #code to email

for i in content:
    print (i)
    #code to email