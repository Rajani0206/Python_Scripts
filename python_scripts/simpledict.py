mydict={
"name": "Rajani",
"id": 1234,
"domain": ["devops","SFDC","cloud"],
"tool":{"os": ["linux","windows"],"cloud" : "AWS"}
}
print(mydict)
print(mydict["id"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["tool"])
print(mydict["tool"]["os"])
print(mydict["tool"]["os"][0])


mydict["place"]="Bangalore"
mydict["place"]=["Bangalore","pune"]
print(mydict)

mydict1={
        "name1" :"Ramya"
        }
mydict.update(mydict1)
print(mydict)
