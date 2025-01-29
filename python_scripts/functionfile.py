def display_content(filename): #filename is a argument we are passing for function
    with open(filename,"r") as fh:
        print(fh.read())
    return filename, "ab", "num"

file_name= "test.txt"
var1, var2, var3  = display_content(file_name) # display_content is a user definded function and we can use any name except keywords

