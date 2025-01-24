demo_dict={
        "Name":"Rajani",
        "Place":"Bangalore",
        "Company":"XYZ",
        "User_ID":123
    }
print(demo_dict)
print("\n")
if "Place" in demo_dict:
    print("Place Key is present\n")
else:
    print("Place Key is not presnt")

if "Bangalore" in demo_dict.values():
    print("Value Bangalore is present\n")
else:
    print("Valye Bangalore is not present")

if demo_dict["Company"]== "XYZ":
    print("Key value pair matches\n")
else:
    print("Key value pair does not match")

if demo_dict["Company"]== "ABC":
    print("Key value pair matches")
else:
    print("Key value pair does not match")    
