import os

def open_license_notice(filename,path): #filename is a argument we are passing for function
    with open(filename,"r") as fh:
        print(fh.read())
    return filename,path


for root,dir,files in os.walk("/home/ubuntu"):
    for file in files:
        if file.lower().startswith(('license','notice')):
            path=print(f"Path of the file \n{root}/{file}")
            print("-------------------------------------------")
            print("Content of file ---")
            file_name= os.path.join(root,file)
            var,var1= open_license_notice(file_name,path)
            


