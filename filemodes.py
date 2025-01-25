with open("sample.py","r") as fh: # fh contains the address of the file when we open it will point to the first character of the file we can use any name
    content = fh.read()
    print(content)
    fh.close() # close() function to close file

with open("test.txt","w") as fh:
     fh.write("Hello world")

with open("test.txt", "r") as fh:
    content1 = fh.read()
    print(content1)

with open("test.txt","a") as fh:
    fh.write("\n Welcome to class")

with open("test.txt","r") as fh:
     print(fh.read())

