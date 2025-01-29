import json
import sys
import requests
import tarfile #module to untarfile

with open("test.json", "r") as fh:
    json_data=json.load(fh)    #load is a function used to read the data from file in json  #loads used to read the data from strings
    #print(json_data)


file_path= "/home/ubuntu/behave.tar.gz"
for ele in json_data:
    #for key, value in ele.items():
        #print(key) 
        #print(value)
    source_url=ele["Source URL"]
    response = requests.get(source_url) # request uses 3 functins which are get put and delete - get is a function used to download a file, put is used to upload a file, delete is used to delete the file
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("Tar file downloaded successfully.")
    break

file = tarfile.open("/home/ubuntu/behave.tar.gz")

file.extractall('/home/ubuntu/')

        #print("-----------------------------------------------------")
    #print(ele)
#sys.exit()
