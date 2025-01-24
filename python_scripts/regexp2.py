import re

email_data="phaninandigam <phaninandigam@gmail.com>, chetan <cheatn@gmail.com>, Harish <Harish@gmail.com>"
result= re.search(r"phani", email_data)
print(result)

result= re.search(r"phanin", email_data)
print(result)

result= re.findall(r"pha", email_data)
print(result)

result= re.search(r"pha[n,m]", email_data)
print(result)


result= re.search(r"pha[n,m,i]{2}", email_data)
print(result)

result= re.search(r"pha[a-z]", email_data)
print(result)

result= re.search(r"pha[a-z]{2}", email_data)
print(result)

result= re.search(r"pha[a-z]+", email_data)
print(result)

result= re.search(r"pha[a-z,A-Z,0-9]+", email_data)
print(result)

print("\nWith search function")
result= re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("\nWith find function")
result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("------------")
result= re.findall(r"pha[a-zA-z@.]+", email_data)
print(result)

print("------------")
result= re.search(r"pha[a-zA-z@.]+", email_data)
print(result)


print("------------\w")
result= re.search(r"\w+@\w+\.\w+", email_data)
print(result)

result= re.search(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])

result= re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])
