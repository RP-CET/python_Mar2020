#opens a file, create new if doesn't exist, for content writing
helloFile = open("hello2.txt", "w")
helloFile.write("This is a line\n")
helloFile.close()

#opens the said file for content reading
helloFile = open("hello2.txt")
print(helloFile.read())
helloFile.close()

#opens the same file for appending text
helloFile = open("hello2.txt", "a")
helloFile.write("This is another line\n")
helloFile.close()

#reopens the said file for content reading
helloFile = open("hello2.txt")
print(helloFile.read())
helloFile.close()

