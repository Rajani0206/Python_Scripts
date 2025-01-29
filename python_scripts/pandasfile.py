import pandas as pd
import json


#def check_str(x):
 #   if isinstance(x, str):  #isinstance is a specific function in python to check specific type
  #      x.strip()
   # else:
    #    x

def read_excel_content(excel_file_path, json_file_path):
    data=pd.read_excel(excel_file_path, sheet_name= "Sheet1")
    #print(data)
    data1= data.applymap(lambda x: x.strip() if isinstance (x, str) else x)
    data1.to_json(json_file_path, orient='records', indent=2)
    print("Excel file is converted to Json")
    #lamdda used to define many functions as single function
    #applymap is a function which used to read each element by element



#print(dir(pd))

excel_file_path= "sample.xlsx"


json_file_path="test.json"
read_excel_content(excel_file_path,json_file_path)


data = {
        "name": "Rajani",
        "id": "123"
        }

data1 = '{"name" : "Rajani", "id" : "123"}'
