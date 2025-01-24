import re

email_data="rajanisc  <rajanisc15@gmail.com>, ramya  <test@gmail.com>, abc  <abc@gmail.com>"
result= re.search(r"ra", email_data)
print(result)

print("----------------------------------------------")

result= re.findall(r"ra",email_data)
print(result)
print("----------------------------------------------")

result= re.search(r"raj[a,m]", email_data)
print(result)
print("----------------------------------------------")

result=re.search(r"raj[a-z]", email_data)
print(result)
print("----------------------------------------------")

result=re.search(r"raj[a-z]{2}", email_data)
print(result)
print("----------------------------------------------")

result=re.search(r"raj[a-z]+", email_data)
print(result)
print("----------------------------------------------")

result=re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)
print("----------------------------------------------")

result=re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)
